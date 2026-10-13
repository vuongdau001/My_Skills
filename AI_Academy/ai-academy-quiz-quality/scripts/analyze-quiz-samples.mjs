#!/usr/bin/env node

import fs from 'node:fs';

function valueAfter(flag, fallback = null) {
  const index = process.argv.indexOf(flag);
  return index >= 0 ? process.argv[index + 1] : fallback;
}

const blueprintPath = valueAfter('--blueprint');
const sampleSize = Number(valueAfter('--sample-size', '6'));
const minObjectives = Number(valueAfter('--min-objectives', '2'));
const minApplied = Number(valueAfter('--min-applied', '3'));
if (!blueprintPath || !Number.isInteger(sampleSize) || sampleSize < 1) {
  console.error('Usage: analyze-quiz-samples.mjs --blueprint <file> [--sample-size 6] [--min-objectives 2] [--min-applied 3]');
  process.exit(2);
}

let blueprint;
try {
  blueprint = JSON.parse(fs.readFileSync(blueprintPath, 'utf8'));
} catch (error) {
  console.error(`Invalid blueprint JSON: ${error.message}`);
  process.exit(2);
}

const items = Array.isArray(blueprint.items) ? blueprint.items : [];
if (items.length < sampleSize) {
  console.error(`Blueprint has ${items.length} items, fewer than sample size ${sampleSize}.`);
  process.exit(2);
}

const totalCombinationLimit = 200000;
const combinations = [];
function enumerate(start, chosen) {
  if (combinations.length > totalCombinationLimit) return;
  if (chosen.length === sampleSize) {
    combinations.push([...chosen]);
    return;
  }
  for (let i = start; i <= items.length - (sampleSize - chosen.length); i += 1) {
    chosen.push(i);
    enumerate(i + 1, chosen);
    chosen.pop();
  }
}
enumerate(0, []);

if (combinations.length > totalCombinationLimit) {
  console.error(`More than ${totalCombinationLimit} combinations; reduce scope or add deterministic simulation for this bank.`);
  process.exit(2);
}

let objectivePass = 0;
let appliedPass = 0;
let bothPass = 0;
let worstObjectiveCount = Number.POSITIVE_INFINITY;
let worstAppliedCount = Number.POSITIVE_INFINITY;
for (const indexes of combinations) {
  const sample = indexes.map((index) => items[index]);
  const objectiveCount = new Set(sample.flatMap((item) => Array.isArray(item.objectiveIds) ? item.objectiveIds : [])).size;
  const appliedCount = sample.filter((item) => item.cognitiveLevel === 'apply' || item.cognitiveLevel === 'analyze').length;
  if (objectiveCount >= minObjectives) objectivePass += 1;
  if (appliedCount >= minApplied) appliedPass += 1;
  if (objectiveCount >= minObjectives && appliedCount >= minApplied) bothPass += 1;
  worstObjectiveCount = Math.min(worstObjectiveCount, objectiveCount);
  worstAppliedCount = Math.min(worstAppliedCount, appliedCount);
}

const percent = (value) => `${(100 * value / combinations.length).toFixed(2)}%`;
console.log(JSON.stringify({
  moduleId: blueprint.moduleId,
  poolSize: items.length,
  sampleSize,
  combinations: combinations.length,
  thresholds: { minObjectives, minApplied },
  passRate: {
    objectiveCoverage: percent(objectivePass),
    appliedOrAnalyze: percent(appliedPass),
    both: percent(bothPass),
  },
  worstCase: { objectiveCount: worstObjectiveCount, appliedOrAnalyzeCount: worstAppliedCount },
  note: 'This measures blueprint composition under unstratified sampling; it does not prove item correctness.',
}, null, 2));
