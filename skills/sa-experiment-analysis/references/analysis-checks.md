# Checks for empirical claims

## Before arithmetic

- Construct the run key from factors that identify an evaluation: method/configuration, dataset/split, seed, checkpoint and protocol. Keep rerun attempts separate from independent seeds. Report duplicates and how they were reconciled.
- Record whether the expected population was fixed before measurement. Report completion rate against that denominator as well as scores on valid runs. Missing is not zero unless the metric protocol explicitly assigns zero to failure.
- Confirm metric units, preprocessing, evaluation budget, access to labels, baseline tuning and measurement hardware where relevant. Distinguish practical system comparisons from claims about one isolated component.
- Check for stale files, metric aliases, cached results and incompatible revisions. Hash or otherwise version the inputs. Do not repair source records in place.

## Computation

State the aggregation axis, macro/micro or weighted rule, number of independent units and any exclusions. Compute from unrounded observations where available; a displayed tie does not justify a strict ordering. Paired evaluation uses matched units; task-to-task variation and seed-to-seed variation answer different questions. Bootstrap or other resampling must resample the independent unit, not correlated tokens or repeated rows.

Specify what each interval means and why its assumptions fit. Statistical significance requires an actual named procedure; practical significance requires a domain-relevant magnitude. Multiple exploratory comparisons should be labeled and adjusted where appropriate. If the design cannot support reliable inference, retain descriptive results and identify the missing basis. A claim of significance does not by itself justify choosing post hoc tests under unverified assumptions. Explicitly requested conditional analyses remain possible with their limits stated.

## Claim bounds

Describe measured differences first. Separate descriptive results, matched comparisons, associations, causal claims and population generalization. Inspect reversals, worst cases, sensitivity to aggregation and failed runs. Do not attribute an ablation gap solely to a removed module when compute or training changed too.

The output should let a reader reconstruct the reported comparison from input identifiers, filters, formulas and run IDs. Send the writer exact values, permitted wording and prohibited extrapolations. A suggested sentence in an analysis report is a claim bound; authoring the manuscript belongs to the writing skill.
