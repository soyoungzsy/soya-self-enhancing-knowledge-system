# Security and privacy

## Public-by-default assumption

Treat every committed file, deleted Git object, Issue, pull request, and release asset as potentially public and permanent.

## Never commit

- API keys, tokens, passwords, cookies, private keys, webhook URLs, or `.env` files;
- real company, customer, colleague, user, or project information without explicit permission;
- internal URLs, repository names, system IDs, message IDs, account IDs, or local absolute paths;
- private meeting notes, chat exports, screenshots, operational data, or source documents;
- sanitized text that can still be re-identified through rare names, exact dates, exact amounts, or unique incident details.

## Before every public push

1. Review the staged diff, not only the working tree.
2. Run `python3 scripts/privacy_scan.py .`.
3. Run `python3 -m unittest discover -s tests -v`.
4. Search for organization-specific terms supplied with `--deny`.
5. Confirm that examples are fictional or explicitly licensed for publication.
6. Confirm the repository visibility and destination account.

The scanner is a guardrail, not proof of safety. Human review remains required for semantic re-identification risks.

## Reporting a problem

Open a GitHub security advisory or contact the repository owner privately. Do not paste suspected secrets into a public Issue.
