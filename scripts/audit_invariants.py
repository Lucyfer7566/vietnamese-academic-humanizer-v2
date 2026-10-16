#!/usr/bin/env python3
"""Surface-level invariant warnings between two academic Markdown files.

Not a semantic, plagiarism, or AI-origin detector. Token mismatches require review.
Usage: python3 scripts/audit_invariants.py source.md revised.md [--json]
"""
from __future__ import annotations
import argparse
import collections
import json
from pathlib import Path
import re
import sys

PATTERNS = {
    "numbers": re.compile(r"(?<![\w])[-+−]?(?:\d{1,3}(?:[.,]\d{3})+|\d+)(?:[.,]\d+)?(?:\s?%|\s?(?:ms|s|MB|GB|GHz|MHz|Hz|mV|V|kB|km|kg|mA))?(?![\w])"),
    "bracket_citations": re.compile(r"\[(?:\d{1,4}(?:\s*[-–,]\s*\d{1,4})*)\]"),
    "latex_citations": re.compile(r"\\(?:cite|citep|citet|autocite|parencite)\*?(?:\[[^\]]*\])*\{[^{}]+\}"),
    "doi": re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", re.I),
    "cross_references": re.compile(r"\\(?:ref|eqref|autoref|cref)\{[^{}]+\}"),
    "inline_math": re.compile(r"\$(?!\$)(.+?)(?<!\\)\$(?!\$)|\\\((.*?)\\\)", re.S),
}
SENSITIVE_WORDS = (
    "không", "chưa", "chỉ", "duy nhất", "tất cả", "luôn", "có thể",
    "có khả năng", "gợi ý", "cho thấy", "chứng minh", "gây ra",
    "tương quan", "liên quan", "dự kiến", "đề xuất", "đã",
)


def extract(text: str) -> dict[str, collections.Counter]:
    result = {}
    for label, pattern in PATTERNS.items():
        matches = []
        for match in pattern.finditer(text):
            item = match.group(0)
            if label == "inline_math":
                item = item.strip()
            matches.append(item)
        result[label] = collections.Counter(matches)
    lower = text.lower()
    result["sensitive_phrases"] = collections.Counter({
        phrase: len(re.findall(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", lower))
        for phrase in SENSITIVE_WORDS if re.search(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", lower)
    })
    return result


def compare(a: str, b: str):
    old, new = extract(a), extract(b)
    issues = []
    for label in PATTERNS:
        missing = list((old[label] - new[label]).elements())
        added = list((new[label] - old[label]).elements())
        if missing or added:
            issues.append({"category": label, "missing_from_revision": missing, "new_in_revision": added,
                           "severity": "review"})
    # A change in language markers is a caution only; identical counts do not prove unchanged logic.
    delta = {}
    for key in sorted(set(old["sensitive_phrases"]) | set(new["sensitive_phrases"])):
        v1, v2 = old["sensitive_phrases"][key], new["sensitive_phrases"][key]
        if v1 != v2:
            delta[key] = {"before": v1, "after": v2}
    if delta:
        issues.append({"category": "modality_negation_language_cues", "changes": delta,
                       "severity": "manual_review_only"})
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("revision", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    a = args.source.read_text(encoding="utf-8")
    b = args.revision.read_text(encoding="utf-8")
    issues = compare(a, b)
    payload = {"status": "REVIEW" if issues else "NO_SURFACE_MISMATCH_FOUND",
               "issues": issues,
               "limitations": "Only checks selected surface tokens; no semantic or academic correctness guarantee."}
    if args.as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"STATUS: {payload['status']}")
        if issues:
            for item in issues:
                print(f"- {item['category']}: {json.dumps(item, ensure_ascii=False)}")
        print("NOTE: A clean token comparison does NOT prove that meaning was preserved.")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
