# Verify changes without moving criteria

For issue verification, preserve each stable ID and close criterion. Construct a row with old anchor, current anchor, claimed change, observed change, verdict, confidence, and missing evidence. Verdicts in prose may be partial/unresolved; canonical issue statuses are only those in the [issue record contract](../../../shared/ISSUES.md). Partial progress leaves the existing issue open/verified/contested as appropriate.

For comparison without an issue list, fix only the criteria needed by the user's question and apply them to both versions. Reuse a supplied rubric. Consult [scientific criteria](../../sa-scientific-review/references/scientific-criteria.md) directly only when scientific merit needs a broader rubric; a narrow numerical or wording comparison need not load the scientific-review entrypoint. A two-version comparison can be completed without inventing historical reviewer judgments. If a historical rubric cannot be recovered, label this a new comparison and do not claim score continuity with past reviews.

Classify new observations:

- `revision_regression`: a defect introduced by the revision, with a before/after anchor.
- `previously_undetected`: present in both versions, so relevant to both assessments.
- `newly_revealed_by_evidence`: additional results expose a problem; cite the new evidence.
- `external_standard_change`: changed venue requirements, assessed separately from frozen progress.

A response letter locates changes but is not proof that they exist. Verify the actual table, proof, method, or run record. If a supplied hash/version changes during the check, invalidate dependent resolutions and re-check that exact version before reporting closure. Keep earlier history and append the reason for reopening.

Example: issue REV-001 asks for evaluation on untouched test items. Revised text states that an experiment will be run next month. The issue remains verified and unresolved, with the promise recorded as an author claim. A new table is still insufficient when split provenance is missing. Resolution requires versioned result and split evidence meeting the original criterion.

Version comparison has three separate outputs: relative progress, current readiness, confidence/comparability. Improvement can coexist with remaining major concerns. No averaging of these outputs into one number. A missing current venue policy makes that readiness component unknown.
