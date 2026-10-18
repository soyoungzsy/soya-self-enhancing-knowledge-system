# Soya Personal Self-Enhancing Knowledge System

**Organize scattered notes so you can find them later and use them to make decisions and take action.**

## Start without coding

A **Skill** is a package of instructions that helps an AI follow repeatable steps. A **prompt** is a message you can copy into an AI chat. Try the message below before installing anything.

1. Open the AI chat you normally use and start a new conversation.
2. Copy the complete message below and replace the bracketed example with information you are allowed to share.
3. Compare the reply with the expected result. Missing information should lead to questions, not invented facts.

```text
Turn this fictional reading note into a reusable card: [a book suggests changing one habit at a time; I want to read ten minutes before bed for three days]. Separate the original claim, my interpretation, unknowns, next action and review date. Do not invent sources.
```

**Expected result:** Expect one note card and a clear next action. Save it in a notes app you already know; no specialist software is needed for this first try.

Your AI service may charge fees and handles the text under its own policies. Do not paste work secrets, private contact details or passwords. If a reply is incomplete, name the missing part and add non-sensitive context. You can stop at any time.

The installation and developer sections below are optional for this first try. For questions, use the repository’s **Issues** tab, the public question area, and remove private/work information before posting.



Use local Markdown, Obsidian and Codex to turn information into traceable decisions, actions and reusable knowledge.

[中文](README.md) · [Fictional end-to-end example](examples/end-to-end-example.md) · [Maintenance](MAINTENANCE.md)

## Background and users

Many knowledge bases become link collections or piles of AI output. This method connects source evidence to judgment, action and learning. It suits knowledge workers managing parallel projects, research and notes who want AI help while preserving provenance and control. It does not suit passive collecting, fully automatic decisions or workflows without evidence/acceptance criteria.

## Start without installing a Skill

Download the repository and copy `starter-vault/` to a separate personal directory. Use a Markdown editor; Obsidian is optional. AI-assisted file work requires an appropriately configured host such as Codex, with only the intended workspace accessible. No model, provider account or credits are included. Review the host's current official instructions before using AGENTS.md; this project is not an official OpenAI/Obsidian framework.

If you only have a chat assistant, start with a sanitized input and this prompt:

```text
Use Soya's Log → Orient → Operate → Preserve loop on this authorized input: [...].
Log facts with sources and mark unknowns. Orient by comparing evidence and objections.
Operate with one next action, owner and acceptance evidence. Preserve one reusable
lesson. Do not invent sources, claim I read something, or mark work done without
acceptance. Draft only; do not modify files or external systems.
```

Expect a source-backed note, an explicit next action and a reusable rule, rather than a larger collection of summaries. The fictional example demonstrates the full chain.

## Build one working loop

1. Copy the starter directory without overwriting your existing vault.
2. Define which data stays private, which actions AI may take and what counts as completion.
3. Adapt `templates/AGENTS.example.md` to your actual host and workspace.
4. Run one chain: source input → evidence note → existing project document → next action → real completion evidence → reusable judgment.
5. Expand only after that chain works; see the Chinese-first [30-day plan](docs/09-30-day-build.md).

## Structure and principles

Use `00_System` for navigation/rules, `10_Projects` for active canonical documents, `20_Evidence` for source material, `30_Research` for external investigation, `40_AI_Methods` for prompts/workflows, `50_Knowledge` for stable reusable judgments, `60_Growth` for learning and `90_Inbox` for unresolved routing. Numbers are optional; distinct purposes matter.

Keep one active document per topic. Separate source reliability from confidence in a conclusion. AI generation, human reading, source verification, application and actual completion are separate states. Every note needs meaningful navigation links. Carry corrections into explicit rules rather than expecting AI to infer them. Automate only stable flows with exceptions, acceptance evidence and stopping conditions.

Observe retrieval time, duplicate explanations, rework from bad sources/statuses, false completion and whether reuse improves a real decision—not document counts or AI call volume.

## Templates and documentation

Templates cover collaboration rules, routing, knowledge notes, source evaluation, adversarial review and completion evidence. Documentation covers architecture, information pipelines, Codex collaboration, quality, reading/internalization, automation and publication boundaries. Detailed documentation is Chinese-first; the English entry and fictional example support initial use without claiming every document has been translated.

## Privacy, updates and recovery

The public package uses generalized methods and fictional examples. Do not commit real people/employers, internal URLs, work materials, private vault paths, credentials or unauthorized screenshots. Local-first storage does not establish that your AI provider never receives data; processing/retention follow the chosen host and service. Review permissions and provider charges before connecting sources.

Back up the complete personal vault before applying templates or migrations. Keep user notes separate from the repository. Updating/reverting source does not restore notes modified by AI; recover from the vault backup and verify. Uninstalling the starter method does not require deleting your knowledge. Start with one copied workspace rather than connecting everything.

For broken links, verify paths in your copied vault; for AI not following rules, check the host's supported configuration mechanism and workspace scope. Report sanitized version/environment/reproduction information; never upload private content. See [SECURITY.md](SECURITY.md).

Repository checks: `python3 scripts/privacy_scan.py .` and `python3 -m unittest discover -s tests -v`. Actual results and release status must be recorded separately; source availability is not a formal release or end-to-end validation certificate. [MIT](LICENSE).

## Sources and acknowledgements

See [sources](SOURCES.md) for original authors, references, dependencies and licenses. AI rewriting does not establish original authorship; required third-party notices remain in applicable downloads.

Version: 0.1.1 · [Release / 固定下载](https://github.com/soyoungzsy/soya-self-enhancing-knowledge-system/releases/tag/v0.1.1)
