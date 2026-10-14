# Quiz authoring and review

Use this reference for knowledge-check multiple-choice quizzes. Interactive labs, artifact graders, and simulations need their own assessment contracts.

## 1. Build the blueprint before the items

For each module, map:

`authority concept/locator -> taught claim -> core content -> objective -> theory anchor -> observable operation -> question family -> misconception set`

Record the primary assessment purpose and the exact principle the item reinforces. A core ID alone is not enough: the reviewer must be able to identify which claim or distinction that particular question checks. Use sidecars/review artifacts for this chain while keeping the runtime schema intact.

Choose cognitive demand based on the taught capability. Technical procedures should normally require application; conceptual modules may emphasize discrimination, diagnosis, or trade-off reasoning. Do not raise difficulty beyond the evidence and practice supplied in theory.

Useful question families include:

- concept discrimination;
- technique or scenario application;
- artifact, code, model, table, or data review;
- misconception diagnosis;
- trade-off or decision under constraints.

Avoid enforcing one universal distribution across all subjects. Record and justify the selected distribution in the blueprint. For a 15-item technical bank, a useful starting profile is approximately 3 discrimination, 5 application, 3 artifact review, 2 misconception diagnosis, and 2 trade-off items; adapt it when the capability requires another mix.

When the agreed scope is level-1 knowledge checks, including the [BA/PO profile](ba-po-content-profile.md), the applied starting mix above does not apply. Author recall/understanding of taught concepts, misconceptions and boundaries. Use 15 items for that course without forcing five cores or three items per core, and do not add a novel-case decision or artifact exercise to reach the count. Distinguish internal level labels from Bloom categories, and professional learning goals from the operation actually assessed.

## 2. Create an item card

Before polishing wording, record:

- question ID and objective ID;
- exact theory/source anchor;
- authority concept and taught claim/core IDs, with source versus editorial interpretation;
- cognitive level and question family;
- capability being tested;
- intended learning purpose, with documented versus reviewer-inferred intent;
- reinforcement target: the exact taught principle or distinction feedback should revisit;
- actual learner operation observed in blind solving, compared with intended demand;
- suitability for the lesson, audience, prerequisites, and technical context;
- test basis or evidence supplied in the stem;
- decision rule;
- intended correct answer;
- misconception represented by each distractor;
- ambiguity and assumption risks;
- technical and assessment review verdicts.
- disposition and rationale: KEEP | EDIT_LANGUAGE | REDESIGN | MOVE | REMOVE_OR_REPLACE.

If the author cannot state the decision rule or the misconception behind a distractor, the item is not ready to write.

## 3. Write the stem

The stem must be self-contained, concise, and answerable using the taught model. Include every fact needed to choose the best answer and exclude decorative story detail.

Avoid:

- asking learners to recall names, locations, or incidental case-study events;
- embedding the answer term in the stem when it becomes a lexical cue;
- hidden assumptions about tools, organizations, data, or requirements;
- negative stems unless the negative is conspicuous and necessary;
- asking for an exact number that is only a local teaching heuristic.

## 3a. Terminology rule TERM-EN-01 — English keywords

Applies to theory, stems, options, and explanations in every track.

- **Use the English keyword** practitioners use daily for every domain or technical term (testing, QA, software engineering, the case-study business domain). Vietnamese translations such as "đặc tả", "khiếm khuyết", "bản dựng" slow IT readers and can be misread.
- **Optional first-use gloss.** At the first occurrence in each independent reading unit (the theory page, and each quiz item because runtime samples items randomly) a short Vietnamese gloss may follow: `specification (đặc tả)`, `defect (lỗi trong sản phẩm)`. Afterwards use the keyword alone.
- **Vietnamese is fine for everyday words** with no special technical meaning (khách hàng, kho, đơn hàng, chi phí, rủi ro in a general sense, quy trình, thời gian) when they cannot be misread in context.
- **No ambiguous umbrella words.** Never use "nghiệp vụ" alone where it could mean business rule, business domain, business requirement, or the BA role; choose `business rule`, `business requirement`, `domain`, `business stakeholder`, `domain expert`, or `Business Analyst (BA)`.
- **Consistency.** One concept, one keyword across theory, glossary, stem, options, and explanation. Do not alternate synonyms (e.g. defect / khiếm khuyết / sai sót / lỗi). Keep authority distinctions such as ISTQB error / defect / failure when the prose relies on them.
- **Authority.** Take the keyword from the track's authority (see [authority-registry.md](authority-registry.md); e.g. ISTQB Glossary and CTFL v4.0.1 for testing, GS1 for supply-chain identifiers). If none exists, record "TERM-EN-01, no authority source".
- **Severity.** `BLOCKER` when an ambiguous or mistranslated term changes the correct answer or makes two options defensible; `MAJOR` when it can change the meaning of a claim, stem, or key, or the tested concept is named inconsistently between theory and quiz; `MINOR` when only readability is affected (long Vietnamese rendering, missing gloss, naming drift without meaning change).

Use [terminology-en-keywords.md](terminology-en-keywords.md) as the shared glossary and extend it when a new term is reviewed.

## 4. Write the options

All four options must answer the same question, use comparable granularity, and belong to the same semantic category.

The key must be uniquely best under the supplied facts. Distractors should model distinct authentic mistakes such as:

- confusing adjacent definitions;
- missing a boundary or precondition;
- selecting a valid technique at the wrong time or layer;
- optimizing a local metric while ignoring the release rule;
- treating a heuristic as an absolute;
- confusing evidence of execution with evidence of outcome.

Do not use comic incompetence, moralized wording, irrelevant technology, obvious absolutes, or padded verbosity to make distractors look different. “All of the above” and “none of the above” require exceptional justification.

Keep distractors close enough to require the taught distinction. When checking event versus state, use confusions between event, state and condition; an unrelated role restriction is not a meaningful substitute. Detect options that merely differ in how careful, ethical or responsible they sound. Do not make a knowledge check difficult by introducing unstated policy or unfamiliar case facts.

## 5. Verify the answer by blind solve

Hide `correctIndex`, solve the item, and write the reason before viewing the key. Then compare every option against the same decision rule.

Use these verdicts:

- `CORRECT`: one answer is uniquely best and supported;
- `AMBIGUOUS`: multiple options remain defensible;
- `CONDITIONALLY_CORRECT`: the key needs an unstated assumption;
- `INCORRECT`: the keyed answer is wrong;
- `UNSUPPORTED`: evidence is insufficient.

Only `CORRECT` is release-ready. Repair the stem or options rather than using the explanation to disambiguate after submission.

## 6. Write the explanation

An explanation is a teaching artifact. It should:

1. state the governing principle or decision rule;
2. apply it to specific facts in the stem;
3. reject the closest alternatives by naming their misconception or missing condition.

It must not merely repeat the key, introduce facts absent from the question, overstate the source, or use generic endings that could fit unrelated items.

## 7. Review the bank

Check the complete source pool, not only a hand-picked sample:

- every important objective has adequate coverage;
- repeated wording does not conceal duplicate ideas;
- question families and cognitive levels fit the module;
- correct positions do not form an exploitable pattern;
- correct-option length, vocabulary, specificity, or tone does not reveal the key;
- explanations are not templated or mutually interchangeable;
- every item is strong enough to appear in a random attempt.

For a 15-item, four-option pool, 3–5 keys at each index is a useful anti-pattern guard, not evidence of semantic quality.

## 8. Adversarial review

Try to score without domain knowledge:

- choose the longest or shortest option;
- choose the option repeating stem keywords;
- prefer positive, evidence-oriented, or responsible-sounding prose;
- exploit answer-position cycles;
- read options without the scenario;
- choose the only option with domain vocabulary.

If a heuristic materially exceeds random performance, inspect the affected items. Do not mechanically pad options or invert the cue; remove the underlying asymmetry.

## 9. Random-delivery review

AI Academy normally serves six questions from a larger pool. Inspect whether plausible attempts cover enough objectives and applied reasoning. Exhaustively enumerate combinations when practical; otherwise use deterministic simulation.

Set sample-analysis thresholds according to the agreed scope. A recall/understanding-only bank has `--min-applied 0`; this does not change its cognitive labels into apply/analyze. Report full-bank coverage separately from attempt coverage and from evidence of learning effectiveness.

Content balancing cannot guarantee a balanced attempt under an unstratified sampler. Report residual risk honestly and recommend runtime stratification separately when needed.
