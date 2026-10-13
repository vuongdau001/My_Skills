#!/usr/bin/env node

import fs from 'node:fs';

function valueAfter(flag) {
  const index = process.argv.indexOf(flag);
  return index >= 0 ? process.argv[index + 1] : null;
}

const blueprintPath = valueAfter('--blueprint');
const quizPath = valueAfter('--quiz');
if (!blueprintPath) {
  console.error('Usage: validate-assessment-blueprint.mjs --blueprint <file> [--quiz <quiz.json>]');
  process.exit(2);
}

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

function array(value) {
  return Array.isArray(value) ? value : [];
}

const issues = [];
let blueprint;
try {
  blueprint = readJson(blueprintPath);
} catch (error) {
  console.error(`Invalid blueprint JSON: ${error.message}`);
  process.exit(2);
}

if (!blueprint || typeof blueprint !== 'object' || Array.isArray(blueprint)) issues.push('Blueprint root must be an object.');
if (typeof blueprint.moduleId !== 'string' || !blueprint.moduleId.trim()) issues.push('moduleId is required.');

const objectives = array(blueprint.objectives);
const items = array(blueprint.items);
if (!objectives.length) issues.push('At least one objective is required.');
if (!items.length) issues.push('At least one item is required.');

const objectiveIds = new Set();
for (const [index, objective] of objectives.entries()) {
  if (!objective || typeof objective !== 'object') {
    issues.push(`objectives[${index}] must be an object.`);
    continue;
  }
  if (typeof objective.id !== 'string' || !objective.id.trim()) issues.push(`objectives[${index}].id is required.`);
  else if (objectiveIds.has(objective.id)) issues.push(`Duplicate objective ID: ${objective.id}.`);
  else objectiveIds.add(objective.id);
  if (typeof objective.outcome !== 'string' || !objective.outcome.trim()) issues.push(`objectives[${index}].outcome is required.`);
  if (!array(objective.sourceAnchors).length) issues.push(`objectives[${index}].sourceAnchors must not be empty.`);
}

const validCognitive = new Set(['remember', 'understand', 'apply', 'analyze']);
const itemIds = new Set();
for (const [index, item] of items.entries()) {
  if (!item || typeof item !== 'object') {
    issues.push(`items[${index}] must be an object.`);
    continue;
  }
  if (typeof item.questionId !== 'string' || !item.questionId.trim()) issues.push(`items[${index}].questionId is required.`);
  else if (itemIds.has(item.questionId)) issues.push(`Duplicate question ID: ${item.questionId}.`);
  else itemIds.add(item.questionId);
  const refs = array(item.objectiveIds);
  if (!refs.length) issues.push(`items[${index}].objectiveIds must not be empty.`);
  for (const ref of refs) if (!objectiveIds.has(ref)) issues.push(`items[${index}] references unknown objective ${ref}.`);
  if (!validCognitive.has(item.cognitiveLevel)) issues.push(`items[${index}].cognitiveLevel must be remember, understand, apply, or analyze.`);
  if (typeof item.sourceAnchor !== 'string' || !item.sourceAnchor.trim()) issues.push(`items[${index}].sourceAnchor is required.`);
  if (typeof item.skill !== 'string' || !item.skill.trim()) issues.push(`items[${index}].skill is required.`);
  if (typeof item.questionFamily !== 'string' || !item.questionFamily.trim()) issues.push(`items[${index}].questionFamily is required.`);
  if (typeof item.decisionRule !== 'string' || !item.decisionRule.trim()) issues.push(`items[${index}].decisionRule is required.`);
  if (!Array.isArray(item.distractorMisconceptions) || item.distractorMisconceptions.length !== 3 || item.distractorMisconceptions.some((value) => typeof value !== 'string' || !value.trim())) issues.push(`items[${index}].distractorMisconceptions must contain three non-empty strings.`);
}

for (const objectiveId of objectiveIds) {
  if (!items.some((item) => array(item?.objectiveIds).includes(objectiveId))) issues.push(`Objective ${objectiveId} has no item coverage.`);
}

if (quizPath) {
  let quiz;
  try {
    quiz = readJson(quizPath);
  } catch (error) {
    issues.push(`Invalid quiz JSON: ${error.message}`);
  }
  if (quiz) {
    const quizIds = new Set(array(quiz.questions).map((question) => question?.id).filter(Boolean));
    for (const id of quizIds) if (!itemIds.has(id)) issues.push(`Quiz question ${id} is missing from the blueprint.`);
    for (const id of itemIds) if (!quizIds.has(id)) issues.push(`Blueprint item ${id} is missing from the quiz.`);
  }
}

if (issues.length) {
  console.error(`Blueprint validation failed with ${issues.length} issue(s):`);
  for (const issue of issues) console.error(`- ${issue}`);
  process.exit(1);
}

console.log(`Blueprint valid: ${blueprint.moduleId}; ${objectives.length} objectives; ${items.length} items.`);
