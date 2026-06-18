# Demo Output

This is the output generated from [`examples/subscription-double-charge.json`](../examples/subscription-double-charge.json).

Run it:

```bash
python3 skills/consumer-dispute-assistant/scripts/build_case_pack.py \
  examples/subscription-double-charge.json \
  --out dispute-pack \
  --tone firm \
  --today 2026-06-18
```

## Generated Files

```text
dispute-pack/
├── case_summary.md
├── merchant_refund_request.md
├── payment_dispute_statement.md
├── regulator_complaint.md
└── follow_up_log.md
```

## case_summary.md

```md
# Case Summary

## Parties

- Consumer: Jane Doe
- Merchant/company: Example Streaming
- Product/service: Monthly video subscription

## Dispute

- Type: subscription cancellation failure
- Amount: $29.99
- Disputed charge date: 2026-06-01
- Order/account/ticket ID: INV-12345
- Desired resolution: Cancel the subscription and refund the June charge.

## Issue Statement

I cancelled the subscription before renewal, but the company charged me again on June 1, 2026.

## Timeline

| Date | Event | Evidence |
| --- | --- | --- |
| 2026-05-01 | Started monthly subscription. |  |
| 2026-05-28 | Cancelled in account settings before the next billing period. |  |
| 2026-06-01 | Charged $29.99 after cancellation. |  |
| 2026-06-02 | Emailed support requesting cancellation confirmation and refund. |  |

## Evidence

| Evidence | Notes | File |
| --- | --- | --- |
| Card statement | Shows $29.99 charge from Example Streaming on 2026-06-01. |  |
| Cancellation screenshot | Shows cancellation completed on 2026-05-28. |  |
| Support email | Shows refund request sent on 2026-06-02. |  |

## Prior Contacts

- 2026-06-02 - Email - Asked support to refund the renewal charge; no response yet.

## Open Gaps

- No obvious gaps in the structured intake. User should still verify all facts before sending.
```

## merchant_refund_request.md

```md
Subject: Request for resolution: Example Streaming charge $29.99

Hello Example Streaming support team,

I am requesting help resolving a billing/refund issue for Monthly video subscription.

Summary:

- Amount in dispute: $29.99
- Charge date: 2026-06-01
- Order/account/ticket ID: INV-12345
- Desired resolution: Cancel the subscription and refund the June charge.

Issue:

I cancelled the subscription before renewal, but the company charged me again on June 1, 2026.

Timeline:

- 2026-05-01: Started monthly subscription.
- 2026-05-28: Cancelled in account settings before the next billing period.
- 2026-06-01: Charged $29.99 after cancellation.
- 2026-06-02: Emailed support requesting cancellation confirmation and refund.

Evidence available:

- Card statement: Shows $29.99 charge from Example Streaming on 2026-06-01.
- Cancellation screenshot: Shows cancellation completed on 2026-05-28.
- Support email: Shows refund request sent on 2026-06-02.

Please review this and provide the requested resolution or a written explanation by 2026-06-25. If you need another document from me, please tell me exactly what is missing.

Thank you,

Jane Doe
```

## payment_dispute_statement.md

```md
# Payment Dispute Statement

I am disputing a charge from Example Streaming for $29.99 dated 2026-06-01.

Product/service: Monthly video subscription

Order/account/ticket ID: INV-12345

Reason for dispute:

I cancelled the subscription before renewal, but the company charged me again on June 1, 2026.

Timeline:

- 2026-05-01: Started monthly subscription.
- 2026-05-28: Cancelled in account settings before the next billing period.
- 2026-06-01: Charged $29.99 after cancellation.
- 2026-06-02: Emailed support requesting cancellation confirmation and refund.

I attempted to resolve this with the merchant:

- 2026-06-02 - Email - Asked support to refund the renewal charge; no response yet.

Evidence I can provide:

- Card statement: Shows $29.99 charge from Example Streaming on 2026-06-01.
- Cancellation screenshot: Shows cancellation completed on 2026-05-28.
- Support email: Shows refund request sent on 2026-06-02.

Requested outcome:

Cancel the subscription and refund the June charge.

I certify that the information above is accurate to the best of my knowledge.
```
