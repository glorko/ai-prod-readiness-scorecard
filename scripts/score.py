#!/usr/bin/env python3
"""
Parse an assessment CSV, compute maturity score and recommendation,
and write an MD report with Red/Amber zones.
"""
import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

ZONE_RED = "Red"      # score < 4
ZONE_AMBER = "Amber"  # 4 <= score < 8
ZONE_OK = "OK"        # score >= 8
ZONE_NA = "N/A"

# Recommendation bands: 20% steps (80, 60, 40)
THRESHOLD_HIGH = 80   # ≥80%
THRESHOLD_MID = 60    # 60–80%
THRESHOLD_LOW = 40    # 40–60% vs <40%


def parse_csv(path):
    """Read assessment CSV; return list of dicts with question_id, is_applicable, score, comment."""
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "question_id" not in (reader.fieldnames or []):
            sys.exit("CSV must have header with question_id, is_applicable, score, comment")
        for row in reader:
            qid = (row.get("question_id") or "").strip()
            if not qid:
                continue
            applicable_raw = (row.get("is_applicable") or "").strip().lower()
            is_applicable = applicable_raw in ("yes", "y", "1", "true")
            score_raw = (row.get("score") or "").strip()
            try:
                score = int(score_raw) if score_raw else None
            except ValueError:
                score = None
            if is_applicable and (score is None or score < 1 or score > 10):
                score = None
            comment = (row.get("comment") or "").strip()
            rows.append({
                "question_id": qid,
                "is_applicable": is_applicable,
                "score": score,
                "comment": comment,
            })
    return rows


def zone(score):
    if score is None:
        return ZONE_NA
    if score < 4:
        return ZONE_RED
    if score < 8:
        return ZONE_AMBER
    return ZONE_OK


def compute_score(rows):
    applicable = [r for r in rows if r["is_applicable"] and r["score"] is not None and 1 <= r["score"] <= 10]
    if not applicable:
        return None, 0
    total = sum(r["score"] for r in applicable)
    n = len(applicable)
    percent = round((total / (n * 10)) * 100, 1)
    return percent, n


def recommendation(percent):
    if percent >= THRESHOLD_HIGH:
        return "Ready for production — you're in great shape. Consider a lightweight review (e.g. security or load test) before scaling."
    if percent >= THRESHOLD_MID:
        return "App is fine. Fix Red items and plan improvements for Amber; consider an engineer or consultant for weak areas."
    if percent >= THRESHOLD_LOW:
        return "App is okay to run. Address Red items before production; consider hiring an engineer or a consultant to close gaps."
    return "App needs work. Recommend hiring an engineer (or technical co-founder) before production; use the report to prioritise work."


def build_report(rows, percent, recommendation_text, generated_at):
    red = [r for r in rows if r["is_applicable"] and r["score"] is not None and zone(r["score"]) == ZONE_RED]
    amber = [r for r in rows if r["is_applicable"] and r["score"] is not None and zone(r["score"]) == ZONE_AMBER]
    na = [r for r in rows if not r["is_applicable"]]

    lines = [
        "# Production Readiness Scorecard Report",
        "",
        f"Generated: {generated_at}",
        "",
        "## Overall",
        "",
        f"- **Score:** {percent}%",
        f"- **Recommendation:** {recommendation_text}",
        "",
    ]

    if red:
        lines.extend([
            "## Red zone (score &lt; 4)",
            "",
            "Items that need immediate attention:",
            "",
            "| Question ID | Score | Comment |",
            "|-------------|-------|---------|",
        ])
        for r in red:
            comment_esc = (r["comment"] or "").replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {r['question_id']} | {r['score']} | {comment_esc} |")
        lines.extend(["", ""])

    if amber:
        lines.extend([
            "## Amber zone (score 4–7)",
            "",
            "Items to review and improve:",
            "",
            "| Question ID | Score | Comment |",
            "|-------------|-------|---------|",
        ])
        for r in amber:
            comment_esc = (r["comment"] or "").replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {r['question_id']} | {r['score']} | {comment_esc} |")
        lines.extend(["", ""])

    lines.extend([
        "## All items",
        "",
        "| Question ID | Applicable | Score | Zone | Comment |",
        "|-------------|------------|-------|------|---------|",
    ])
    for r in rows:
        app = "yes" if r["is_applicable"] else "no"
        score_str = str(r["score"]) if r["score"] is not None else ""
        z = zone(r["score"])
        comment_esc = (r["comment"] or "").replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {r['question_id']} | {app} | {score_str} | {z} | {comment_esc} |")
    lines.append("")

    if na:
        lines.extend([
            "## Not applicable",
            "",
            "These items were excluded from scoring:",
            "",
            "| Question ID | Reason |",
            "|-------------|--------|",
        ])
        for r in na:
            comment_esc = (r["comment"] or "").replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {r['question_id']} | {comment_esc} |")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Parse assessment CSV and generate scorecard report")
    parser.add_argument("csv_path", type=Path, help="Path to assessment CSV")
    parser.add_argument("-o", "--output", type=Path, default=None, help="Output MD report path (default: <csv_stem>-report.md)")
    args = parser.parse_args()

    csv_path = args.csv_path
    if not csv_path.is_file():
        sys.exit(f"File not found: {csv_path}")

    rows = parse_csv(csv_path)
    if not rows:
        sys.exit("No valid rows in CSV")

    percent, n_applicable = compute_score(rows)
    if percent is None:
        sys.exit("No applicable scored rows; cannot compute percentage")

    rec = recommendation(percent)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    report_content = build_report(rows, percent, rec, generated_at)

    out_path = args.output
    if out_path is None:
        out_path = csv_path.with_stem(csv_path.stem + "-report").with_suffix(".md")

    out_path.write_text(report_content, encoding="utf-8")

    print(f"Score: {percent}%")
    print(f"Recommendation: {rec}")
    print(f"Report: {out_path}")


if __name__ == "__main__":
    main()
