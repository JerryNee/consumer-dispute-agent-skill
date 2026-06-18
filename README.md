# consumer-dispute-assistant

> Turn a messy refund, subscription, or billing dispute into a clean case pack your agent can actually use.

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-111827)](https://agentskills.io/)
[![Claude](https://img.shields.io/badge/Claude-Skill-6B46C1)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
[![Codex](https://img.shields.io/badge/Codex-Skill-0F766E)](https://developers.openai.com/codex/skills)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Small, boring, useful.

`consumer-dispute-assistant` is an Agent Skill for handling everyday consumer disputes: cancelled subscriptions that keep billing, duplicate charges, refund denials, missing services, bad support loops, and complaint escalation.

It does not pretend to be a lawyer. It helps an agent do the part people usually give up on: collect the facts, organize the evidence, draft the message, and keep a paper trail.

## Why

Most refund tools stop at "write a complaint letter."

Real disputes need more than a letter:

- What happened?
- What evidence exists?
- What is missing?
- Who should be contacted first?
- What should be sent to the merchant?
- What should be saved for a payment dispute?
- What should never be claimed because it is not supported by evidence?

This skill packages that workflow so Claude, Codex, or any Agent Skills-compatible client can follow it consistently.

## Demo

Input:

```text
I cancelled Example Streaming on May 28, 2026, but they charged me $29.99 on June 1.
I have a card statement, a cancellation screenshot, and a support email from June 2.
```

Command:

```bash
python3 skills/consumer-dispute-assistant/scripts/build_case_pack.py \
  examples/subscription-double-charge.json \
  --out dispute-pack \
  --tone firm \
  --today 2026-06-18
```

Output:

```text
dispute-pack/
├── case_summary.md
├── merchant_refund_request.md
├── payment_dispute_statement.md
├── regulator_complaint.md
└── follow_up_log.md
```

Preview:

```text
Subject: Request for resolution: Example Streaming charge $29.99

I cancelled the subscription before renewal, but the company charged me again on June 1, 2026.

Evidence available:
- Card statement: Shows $29.99 charge from Example Streaming on 2026-06-01.
- Cancellation screenshot: Shows cancellation completed on 2026-05-28.
- Support email: Shows refund request sent on 2026-06-02.
```

See the full sample output in [`docs/demo-output.md`](docs/demo-output.md).

## Install

### Codex

```bash
mkdir -p ~/.codex/skills
cp -R skills/consumer-dispute-assistant ~/.codex/skills/
```

Then ask:

```text
Use $consumer-dispute-assistant to build a refund case pack.
```

### Claude

```bash
cd skills
zip -r consumer-dispute-assistant.zip consumer-dispute-assistant
```

Upload `consumer-dispute-assistant.zip` in Claude's custom Skills settings.

## Quickstart

Run the included example:

```bash
python3 skills/consumer-dispute-assistant/scripts/build_case_pack.py \
  examples/subscription-double-charge.json \
  --out dispute-pack \
  --tone firm \
  --today 2026-06-18
```

You get:

```text
dispute-pack/
├── case_summary.md
├── merchant_refund_request.md
├── payment_dispute_statement.md
├── regulator_complaint.md
└── follow_up_log.md
```

Print the JSON shape:

```bash
python3 skills/consumer-dispute-assistant/scripts/build_case_pack.py --print-schema
```

## Example Prompt

```text
Use $consumer-dispute-assistant.

I cancelled Example Streaming on May 28, 2026, but they charged me $29.99 on June 1.
I have a card statement, a cancellation screenshot, and a support email from June 2.

Create:
1. a case summary
2. a merchant refund email
3. a payment dispute statement
4. a next-step plan
```

## What It Handles

| Dispute | Output |
| --- | --- |
| Cancelled subscription still billed | Refund request, evidence timeline, payment dispute statement |
| Duplicate or incorrect charge | Billing correction email, charge comparison, follow-up log |
| Refund denied | Merchant escalation draft, policy/evidence checklist |
| Product not as described | Case summary, return/refund request, complaint draft |
| Service not provided | Demand for performance/refund, timeline, escalation route |
| Support loop with no resolution | Supervisor escalation, regulator/BBB complaint draft |

## What Is Inside

```text
skills/consumer-dispute-assistant/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── evidence-checklist.md
│   ├── escalation-playbooks.md
│   └── safety-boundaries.md
├── assets/templates/
│   ├── case_summary.md
│   ├── merchant_refund_request.md
│   ├── payment_dispute_statement.md
│   ├── regulator_complaint.md
│   └── follow_up_log.md
└── scripts/build_case_pack.py
```

## Design Principles

- Facts first. No invented evidence, no fake receipts, no inflated claims.
- User stays in control. The agent prepares drafts; the user approves external action.
- Escalate gradually. Merchant first, then payment/platform, then complaint channels.
- Keep it portable. Plain Markdown, JSON, and a normal Agent Skills folder.
- Be useful without a server. Bring your own agent, model, and workspace.

## Not A Robot Lawyer

This project is deliberately not a legal-advice product.

It can draft factual complaint materials and help organize evidence. It should not file court documents, impersonate professionals, guarantee refunds, or submit anything externally without explicit user approval.

For jurisdiction-specific deadlines, rights, or filing rules, verify current official sources or talk to a qualified professional.

## Roadmap

- Company-specific playbooks for subscriptions, telecom, travel, and marketplaces
- Official complaint portal references by jurisdiction
- Browser-agent recipes for supervised form filling
- PDF, email, and screenshot evidence extraction helpers
- More real-world examples with private data removed

## Release

- v0.1.0 notes: [`docs/release-notes/v0.1.0.md`](docs/release-notes/v0.1.0.md)

## Contributing

Contributions are welcome if they make the workflow more accurate, safer, or easier to run.

Good PRs:

- add evidence checklists
- improve templates
- add dispute examples
- tighten safety boundaries
- link to official complaint resources

Bad PRs:

- add fake-document generation
- encourage harassment or threats
- market the skill as legal advice
- remove the user confirmation gate

## License

MIT
