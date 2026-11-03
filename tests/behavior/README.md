# Bounded instruction-use checks

These cases require an agent; they are not part of the deterministic unittest suite.
Use [cases.json](cases.json) with the selected package revision. For the resume
case, copy [resume](resume/) into an isolated working directory; retain its input
hashes before and after execution.

Run each revision in a fresh session with the same model configuration and tool
access. Supply the case request, its named skill entrypoints and only its input
artifacts. Do not give the worker the expected answer or another revision's output.
Record actual responses, loaded files, commands and failures before grading.

Compare task completion, evidence limits, extra confirmations, unrelated work and
input mutations. Output length and file reads are descriptive, not quality scores.
Evaluate implicit skill routing separately: explicitly naming a skill does not test
discovery. For stronger evidence use fresh sessions per case and repeated trials.

Recorded execution: [2026-11-02 comparison](../../docs/validation/2026-11-02-behavior.md).
