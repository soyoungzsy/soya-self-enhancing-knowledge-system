# SOYA-个人自增强知识库系统搭建

### SOYA Personal Self-Enhancing Knowledge System

A local-first method for turning meetings, messages, research, data, and AI output into traceable decisions and reusable work with Markdown, Obsidian, and Codex.

## The problem

Most personal knowledge bases optimize for storage. This project optimizes for reuse:

- preserve evidence without drowning in raw input;
- separate active projects, source material, reusable knowledge, and AI workflows;
- keep one canonical document per topic;
- let Codex continue existing work instead of creating parallel drafts;
- distinguish generated, read, verified, applied, and completed;
- turn corrections into durable instructions and templates.

## The loop

```text
Log       capture real inputs and context
Orient    retrieve prior judgment, challenge assumptions, decide boundaries
Operate   turn judgment into actions with explicit ownership and acceptance
Preserve  write results, failures, and reusable rules back into the system
```

## Start here

1. Copy [`starter-vault`](starter-vault/).
2. Adapt [`templates/AGENTS.example.md`](templates/AGENTS.example.md).
3. Run one real workflow from source evidence to an accepted result.
4. Review the [full fictional example](examples/end-to-end-example.md).
5. Follow the [30-day build plan](docs/09-30-day-build.md).

The full documentation is currently Chinese-first. Contributions improving the English edition are welcome.

## Privacy

This repository contains only generalized methods, templates, and fictional examples. Before publishing changes, run:

```bash
python3 scripts/privacy_scan.py .
python3 -m unittest discover -s tests -v
```

## License

[MIT](LICENSE) © SOYA
