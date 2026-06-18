# Evidence Checklist

Use this reference to convert messy screenshots, emails, PDFs, chat logs, and user notes into a factual dispute record.

## Intake Fields

Required when available:

- `consumer_name`: User's preferred signing name.
- `merchant_name`: Company or merchant.
- `product_or_service`: What was purchased or subscribed to.
- `dispute_type`: Subscription, duplicate charge, unauthorized charge, refund denial, service failure, product issue, travel/lodging, telecom/utility, banking/payment, other.
- `amount`: Disputed amount.
- `currency`: Currency symbol or code.
- `charge_date`: Date of disputed charge.
- `purchase_date`: Original purchase date.
- `cancellation_date`: Date user cancelled, if relevant.
- `order_id`: Order, invoice, receipt, confirmation, account, or ticket ID.
- `payment_method`: Card, bank, PayPal, Apple Pay, app store, marketplace, etc. Use last four digits only.
- `desired_resolution`: Refund, cancellation, replacement, correction, compensation, access restoration, explanation, or apology.
- `issue_summary`: One to three factual sentences.
- `timeline`: Date/event pairs.
- `evidence`: List of documents or screenshots with labels.
- `prior_contacts`: Support messages, phone calls, ticket IDs, dates, and responses.

## Evidence Strength

Strong evidence:

- Receipt, invoice, or statement showing amount/date/merchant.
- Cancellation confirmation or screenshot showing cancellation attempt.
- Terms, refund policy, trial end date, shipping promise, or service-level promise visible at purchase time.
- Merchant chat/email where the company acknowledges the issue.
- Delivery tracking, appointment records, outage notices, hotel/flight disruption notices.
- Bank or card statement showing duplicate or unauthorized charge.

Medium evidence:

- User calendar reminders, notes, or call logs.
- Screenshots without visible date or account context.
- A policy page captured after purchase.
- User recollection of a phone call without ticket ID.

Weak or missing evidence:

- Claims with no date, amount, or merchant.
- Screenshots that can be interpreted multiple ways.
- Hearsay from third parties.
- Edited images, generated receipts, or unverifiable records.

Never create or suggest fake receipts, fake screenshots, fabricated cancellation records, or false statements.

## Redaction

Redact before sharing outside the user's private workspace:

- Full card numbers, bank account numbers, SSNs, tax IDs, passwords, access tokens.
- Full home address unless required by an official form.
- Medical, family, immigration, or employment details not needed for the dispute.
- Private messages from unrelated third parties.

Keep:

- Last four digits of a card/account when needed.
- Dates, amount, merchant, order ID, ticket ID.
- User name and contact info only if the user is ready to send/file.

## Timeline Pattern

Use this structure:

| Date | Event | Evidence |
| --- | --- | --- |
| YYYY-MM-DD | User purchased/subscribed/cancelled/contacted support | Receipt, screenshot, email |

If the exact date is unknown, write `Approx. Month YYYY` and mark it as an uncertainty.

## Evidence Gap Prompts

Ask only for facts that matter. Useful prompts:

- "Do you have a receipt, invoice, or card statement showing the charge?"
- "Do you have a cancellation confirmation or screenshot of the cancellation page?"
- "What exact outcome do you want: refund, cancellation, replacement, or correction?"
- "Have you contacted support already? If yes, what date and what ticket ID?"
- "Was the charge through the merchant directly, an app store, PayPal, a bank card, or a marketplace?"
