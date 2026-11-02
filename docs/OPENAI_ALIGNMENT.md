# Historical design references

This is a record of the 2026-10-06 review of version 0.1.2, not a current compatibility assessment or certification. It has not been rerun for subsequent revisions.

The review used these sources:

- [Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills): distinguish structural checks from observed behavior and retain failed attempts.
- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): narrow descriptions, conditional resource loading and task-sized workflows.
- [Skills API guide](https://developers.openai.com/api/docs/guides/tools-skills): skill organization; API integration was not implemented or verified.
- [Build skills](https://developers.openai.com/plugins/build/skills) and [plugin packaging](https://developers.openai.com/plugins/build/plugins): entrypoints, resources and plugin layout.

Current local checks and historical behavior results are tracked in [evaluation](EVALUATION.md); host-specific observations are in [host acceptance](HOST_ACCEPTANCE.md). Consult current official documentation before changing integration behavior.
