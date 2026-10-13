#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';

function usage() {
  console.error('Usage: audit-quiz-bank.mjs --root <repo> [--track <track>] [--module <text>] [--json] [--strict]');
}

function parseArgs(argv) {
  const out = { root: '.', track: null, module: null, json: false, strict: false };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--root' || arg === '--track' || arg === '--module') {
      if (!argv[i + 1]) throw new Error(`${arg} requires a value`);
      out[arg.slice(2)] = argv[++i];
    } else if (arg === '--json') out.json = true;
    else if (arg === '--strict') out.strict = true;
    else if (arg === '--help' || arg === '-h') return null;
    else throw new Error(`Unknown argument: ${arg}`);
  }
  return out;
}

function walk(dir, result = []) {
  if (!fs.existsSync(dir)) return result;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, result);
    else if (entry.isFile() && (entry.name.endsWith('.quiz.json') || entry.name === 'quiz.json')) result.push(full);
  }
  return result;
}

function normalize(value) {
  return String(value ?? '').toLocaleLowerCase('vi').normalize('NFKD').replace(/[\u0300-\u036f]/g, '').replace(/đ/g, 'd').replace(/[^a-z0-9]+/g, ' ').trim();
}

function tokens(value) {
  const stop = new Set(['va', 'la', 'cua', 'cho', 'mot', 'nhung', 'trong', 'voi', 'duoc', 'khi', 'thi', 'theo', 'nay', 'do']);
  return new Set(normalize(value).split(/\s+/).filter((word) => word.length >= 4 && !stop.has(word)));
}

function overlapScore(stem, option) {
  const left = tokens(stem);
  const right = tokens(option);
  let score = 0;
  for (const token of right) if (left.has(token)) score += 1;
  return score;
}

function combination(n, k) {
  if (k < 0 || k > n) return 0;
  k = Math.min(k, n - k);
  let value = 1;
  for (let i = 1; i <= k; i += 1) value = (value * (n - k + i)) / i;
  return Math.round(value);
}

function finding(severity, code, file, item, message, evidence = {}) {
  return { severity, code, file, item, message, evidence };
}

function auditFile(file, root) {
  const findings = [];
  let raw;
  try {
    raw = JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch (error) {
    return { file: path.relative(root, file), questionCount: 0, findings: [finding('BLOCKER', 'INVALID_JSON', path.relative(root, file), null, error.message)] };
  }
  const rel = path.relative(root, file);
  const questions = Array.isArray(raw.questions) ? raw.questions : [];
  if (!Array.isArray(raw.questions)) findings.push(finding('BLOCKER', 'MISSING_QUESTIONS', rel, null, 'Root object must contain a questions array.'));
  const ids = new Set();
  const stems = new Map();
  const optionSets = new Map();
  const explanationTails = new Map();
  const keyCounts = [0, 0, 0, 0];
  let longestKeyCount = 0;
  let uniqueHighestOverlapKeyCount = 0;

  questions.forEach((q, index) => {
    const item = q?.id ?? `index:${index}`;
    if (!q || typeof q !== 'object' || Array.isArray(q)) {
      findings.push(finding('BLOCKER', 'INVALID_ITEM', rel, item, 'Question must be an object.'));
      return;
    }
    if (typeof q.id !== 'string' || !q.id.trim()) findings.push(finding('BLOCKER', 'MISSING_ID', rel, item, 'Question ID is missing.'));
    else if (ids.has(q.id)) findings.push(finding('BLOCKER', 'DUPLICATE_ID', rel, item, 'Question ID is duplicated.'));
    else ids.add(q.id);
    if (typeof q.question !== 'string' || !q.question.trim()) findings.push(finding('BLOCKER', 'MISSING_STEM', rel, item, 'Question text is missing.'));
    const stemKey = normalize(q.question);
    if (stemKey && stems.has(stemKey)) findings.push(finding('MAJOR', 'DUPLICATE_STEM', rel, item, `Exact normalized stem duplicates ${stems.get(stemKey)}.`));
    else if (stemKey) stems.set(stemKey, item);

    if (!Array.isArray(q.options) || q.options.length !== 4) {
      findings.push(finding('BLOCKER', 'OPTION_COUNT', rel, item, 'Question must have exactly four options.'));
      return;
    }
    const normalizedOptions = q.options.map(normalize);
    if (new Set(normalizedOptions).size !== 4) findings.push(finding('BLOCKER', 'DUPLICATE_OPTIONS', rel, item, 'Options must be distinct.'));
    const optionSet = [...normalizedOptions].sort().join('|');
    if (optionSets.has(optionSet)) findings.push(finding('MAJOR', 'REUSED_OPTION_SET', rel, item, `Option set repeats ${optionSets.get(optionSet)}.`));
    else optionSets.set(optionSet, item);

    if (!Number.isInteger(q.correctIndex) || q.correctIndex < 0 || q.correctIndex > 3) {
      findings.push(finding('BLOCKER', 'INVALID_KEY', rel, item, 'correctIndex must be an integer from 0 to 3.'));
    } else {
      keyCounts[q.correctIndex] += 1;
      const lengths = q.options.map((option) => normalize(option).length);
      if (lengths[q.correctIndex] === Math.max(...lengths) && lengths.filter((value) => value === lengths[q.correctIndex]).length === 1) longestKeyCount += 1;
      const overlaps = q.options.map((option) => overlapScore(q.question, option));
      if (overlaps[q.correctIndex] === Math.max(...overlaps) && overlaps.filter((value) => value === overlaps[q.correctIndex]).length === 1) uniqueHighestOverlapKeyCount += 1;
    }

    if (typeof q.sourceRef !== 'string' || !q.sourceRef.startsWith('theory/')) findings.push(finding('BLOCKER', 'INVALID_SOURCE_REF', rel, item, 'sourceRef must point to theory content.'));
    if (typeof q.reviewedAt !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(q.reviewedAt)) findings.push(finding('MAJOR', 'INVALID_REVIEW_DATE', rel, item, 'reviewedAt must use YYYY-MM-DD.'));
    if (typeof q.explanation !== 'string' || !q.explanation.trim()) findings.push(finding('BLOCKER', 'MISSING_EXPLANATION', rel, item, 'Explanation is missing.'));
    else {
      const words = normalize(q.explanation).split(/\s+/).filter(Boolean);
      const tail = words.slice(-8).join(' ');
      if (tail) {
        const list = explanationTails.get(tail) ?? [];
        list.push(item);
        explanationTails.set(tail, list);
      }
    }
  });

  if (questions.length && questions.length < 6) findings.push(finding('BLOCKER', 'POOL_TOO_SMALL', rel, null, `Pool has ${questions.length} questions; current runtime expects at least 6.`));
  if (questions.length > 20) findings.push(finding('BLOCKER', 'POOL_TOO_LARGE', rel, null, `Pool has ${questions.length} questions; current loader allows at most 20.`));
  if (questions.length === 15 && keyCounts.some((count) => count < 3 || count > 5)) findings.push(finding('MAJOR', 'KEY_DISTRIBUTION', rel, null, 'For a 15-item pool, one or more key positions fall outside the 3–5 anti-pattern guard.', { keyCounts }));
  if (questions.length >= 10 && longestKeyCount / questions.length >= 0.6) findings.push(finding('MAJOR', 'LONGEST_OPTION_CUE', rel, null, 'The uniquely longest option is keyed in at least 60% of items.', { longestKeyCount, total: questions.length }));
  if (questions.length >= 10 && uniqueHighestOverlapKeyCount / questions.length >= 0.6) findings.push(finding('MAJOR', 'LEXICAL_OVERLAP_CUE', rel, null, 'The key has uniquely highest stem-token overlap in at least 60% of items.', { uniqueHighestOverlapKeyCount, total: questions.length }));
  for (const [tail, items] of explanationTails) {
    if (items.length >= 3) findings.push(finding('MAJOR', 'EXPLANATION_TAIL_REUSE', rel, null, `The same normalized explanation ending appears in ${items.length} items.`, { items, tail }));
  }

  return {
    file: rel,
    questionCount: questions.length,
    keyCounts,
    longestKeyCount,
    uniqueHighestOverlapKeyCount,
    possibleSixQuestionSamples: combination(questions.length, 6),
    findings,
  };
}

let args;
try {
  args = parseArgs(process.argv.slice(2));
  if (!args) {
    usage();
    process.exit(0);
  }
} catch (error) {
  usage();
  console.error(error.message);
  process.exit(2);
}

const root = path.resolve(args.root);
const curriculum = path.join(root, 'curriculum');
const searchRoot = args.track ? path.join(curriculum, args.track) : curriculum;
let files = walk(searchRoot).sort();
if (args.module) files = files.filter((file) => file.includes(args.module));
if (!files.length) {
  console.error('No quiz files matched the requested scope.');
  process.exit(2);
}

const audited = files.map((file) => auditFile(file, root));
const allFindings = audited.flatMap((entry) => entry.findings);
const output = {
  scope: { root, track: args.track, module: args.module, files: audited.length },
  totals: {
    questions: audited.reduce((sum, entry) => sum + entry.questionCount, 0),
    blockers: allFindings.filter((item) => item.severity === 'BLOCKER').length,
    majors: allFindings.filter((item) => item.severity === 'MAJOR').length,
  },
  disclaimer: 'Static evidence only: this audit cannot certify domain correctness, cognitive validity, or a unique best answer.',
  files: audited,
};

if (args.json) console.log(JSON.stringify(output, null, 2));
else {
  console.log(`Quiz files: ${output.totals.questions} questions across ${audited.length} files`);
  console.log(`Findings: ${output.totals.blockers} blocker, ${output.totals.majors} major`);
  console.log(output.disclaimer);
  for (const entry of audited) {
    if (!entry.findings.length) continue;
    console.log(`\n${entry.file}`);
    for (const item of entry.findings) console.log(`- [${item.severity}] ${item.code}${item.item ? ` (${item.item})` : ''}: ${item.message}`);
  }
}

if (output.totals.blockers > 0 || (args.strict && output.totals.majors > 0)) process.exitCode = 1;
