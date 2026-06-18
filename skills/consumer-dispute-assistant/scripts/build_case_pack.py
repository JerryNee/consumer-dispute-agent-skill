#!/usr/bin/env python3
"""Build a Markdown consumer dispute case pack from a JSON intake file."""

from __future__ import annotations

import argparse
import json
from datetime import date, timedelta
from pathlib import Path
from string import Template
from typing import Any


SCHEMA: dict[str, Any] = {
    "consumer_name": "Jane Doe",
    "merchant_name": "Example Streaming",
    "product_or_service": "Monthly subscription",
    "dispute_type": "subscription cancellation failure",
    "amount": "29.99",
    "currency": "$",
    "charge_date": "2026-06-01",
    "purchase_date": "2026-05-01",
    "cancellation_date": "2026-05-28",
    "order_id": "INV-12345",
    "payment_method": "Visa ending 1234",
    "desired_resolution": "Cancel the subscription and refund the June charge.",
    "issue_summary": "I cancelled before renewal but was charged again.",
    "timeline": [
        {"date": "2026-05-01", "event": "Started subscription."},
        {"date": "2026-05-28", "event": "Cancelled in account settings."},
        {"date": "2026-06-01", "event": "Charged after cancellation."}
    ],
    "evidence": [
        {"label": "Card statement", "notes": "Shows $29.99 charge on 2026-06-01."},
        {"label": "Cancellation screenshot", "notes": "Shows cancellation on 2026-05-28."}
    ],
    "prior_contacts": [
        {"date": "2026-06-02", "channel": "Email", "summary": "Asked support for refund; no response."}
    ]
}


def missing() -> str:
    return "Needs user input"


def value(data: dict[str, Any], key: str) -> str:
    raw = data.get(key)
    if raw is None or raw == "":
        return missing()
    return str(raw).strip()


def list_items(data: dict[str, Any], key: str) -> list[Any]:
    raw = data.get(key, [])
    return raw if isinstance(raw, list) else []


def bullet_list(items: list[str]) -> str:
    if not items:
        return f"- {missing()}"
    return "\n".join(f"- {item}" for item in items)


def timeline_rows(data: dict[str, Any]) -> list[str]:
    rows = []
    for item in list_items(data, "timeline"):
        if isinstance(item, dict):
            rows.append(f"{item.get('date', missing())}: {item.get('event', missing())}")
        else:
            rows.append(str(item))
    return rows


def evidence_rows(data: dict[str, Any]) -> list[str]:
    rows = []
    for item in list_items(data, "evidence"):
        if isinstance(item, dict):
            rows.append(f"{item.get('label', missing())}: {item.get('notes', missing())}")
        else:
            rows.append(str(item))
    return rows


def contact_rows(data: dict[str, Any]) -> list[str]:
    rows = []
    for item in list_items(data, "prior_contacts"):
        if isinstance(item, dict):
            pieces = [
                item.get("date", missing()),
                item.get("channel", missing()),
                item.get("summary", missing()),
            ]
            rows.append(" - ".join(str(piece) for piece in pieces))
        else:
            rows.append(str(item))
    return rows


def markdown_table(rows: list[str], headers: tuple[str, str, str]) -> str:
    if not rows:
        return f"| {headers[0]} | {headers[1]} | {headers[2]} |\n| --- | --- | --- |\n| {missing()} | {missing()} | {missing()} |"
    out = [f"| {headers[0]} | {headers[1]} | {headers[2]} |", "| --- | --- | --- |"]
    for row in rows:
        first, _, rest = row.partition(":")
        out.append(f"| {first.strip()} | {rest.strip() or row.strip()} |  |")
    return "\n".join(out)


def open_gaps(data: dict[str, Any]) -> str:
    required = [
        "consumer_name",
        "merchant_name",
        "product_or_service",
        "amount",
        "charge_date",
        "desired_resolution",
        "issue_summary",
    ]
    gaps = [key for key in required if not data.get(key)]
    if not list_items(data, "evidence"):
        gaps.append("evidence")
    if not list_items(data, "timeline"):
        gaps.append("timeline")
    if not gaps:
        return "- No obvious gaps in the structured intake. User should still verify all facts before sending."
    return "\n".join(f"- {key}: {missing()}" for key in gaps)


def template_context(data: dict[str, Any]) -> dict[str, str]:
    today = date.today()
    response_deadline = today + timedelta(days=7)
    timeline = timeline_rows(data)
    evidence = evidence_rows(data)
    contacts = contact_rows(data)
    return {
        "consumer_name": value(data, "consumer_name"),
        "merchant_name": value(data, "merchant_name"),
        "product_or_service": value(data, "product_or_service"),
        "dispute_type": value(data, "dispute_type"),
        "amount": value(data, "amount"),
        "currency": value(data, "currency") if data.get("currency") else "$",
        "charge_date": value(data, "charge_date"),
        "order_id": value(data, "order_id"),
        "payment_method": value(data, "payment_method"),
        "desired_resolution": value(data, "desired_resolution"),
        "issue_summary": value(data, "issue_summary"),
        "timeline_bullets": bullet_list(timeline),
        "timeline_table": markdown_table(timeline, ("Date", "Event", "Evidence")),
        "evidence_bullets": bullet_list(evidence),
        "evidence_table": markdown_table(evidence, ("Evidence", "Notes", "File")),
        "prior_contacts": bullet_list(contacts),
        "open_gaps": open_gaps(data),
        "today": today.isoformat(),
        "response_deadline": response_deadline.isoformat(),
    }


def merchant_closing(tone: str, response_deadline: str) -> str:
    if tone == "friendly":
        return (
            "Could you please review this and help resolve it? If I am missing "
            "anything, please let me know what document or detail you need."
        )
    if tone == "final":
        return (
            "Please provide the requested resolution or a written explanation by "
            f"{response_deadline}. If this cannot be resolved directly, I may consider "
            "appropriate next steps such as a payment dispute or a consumer complaint."
        )
    return (
        "Please review this and provide the requested resolution or a written "
        f"explanation by {response_deadline}. If you need another document from me, "
        "please tell me exactly what is missing."
    )


def render_template(template_path: Path, context: dict[str, str]) -> str:
    text = template_path.read_text(encoding="utf-8")
    return Template(text.replace("{{", "${").replace("}}", "}")).safe_substitute(context)


def build_pack(data: dict[str, Any], out_dir: Path, tone: str) -> None:
    skill_root = Path(__file__).resolve().parents[1]
    templates_dir = skill_root / "assets" / "templates"
    out_dir.mkdir(parents=True, exist_ok=True)
    context = template_context(data)
    context["tone"] = tone
    context["merchant_closing"] = merchant_closing(tone, context["response_deadline"])

    files = {
        "case_summary.md": "case_summary.md",
        "merchant_refund_request.md": "merchant_refund_request.md",
        "payment_dispute_statement.md": "payment_dispute_statement.md",
        "regulator_complaint.md": "regulator_complaint.md",
        "follow_up_log.md": "follow_up_log.md",
    }
    for output_name, template_name in files.items():
        rendered = render_template(templates_dir / template_name, context)
        (out_dir / output_name).write_text(rendered.rstrip() + "\n", encoding="utf-8")

    index = [
        "# Dispute Pack Index",
        "",
        f"- Tone requested: {tone}",
        "- Review all facts before sending or filing.",
        "- Do not submit any external action without user approval.",
        "",
        "## Files",
    ]
    index.extend(f"- `{name}`" for name in files)
    (out_dir / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a consumer dispute Markdown case pack.")
    parser.add_argument("input_json", nargs="?", help="Path to JSON intake file.")
    parser.add_argument("--out", default="dispute-pack", help="Output directory.")
    parser.add_argument("--tone", choices=["friendly", "firm", "final"], default="firm")
    parser.add_argument("--print-schema", action="store_true", help="Print example JSON schema.")
    args = parser.parse_args()

    if args.print_schema:
        print(json.dumps(SCHEMA, indent=2))
        return 0

    if not args.input_json:
        parser.error("input_json is required unless --print-schema is used")

    input_path = Path(args.input_json)
    data = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("Intake JSON must be an object.")

    build_pack(data, Path(args.out), args.tone)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
