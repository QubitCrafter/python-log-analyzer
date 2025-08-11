from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict

from .analyzer import count_log_levels, LOG_LEVELS


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="log-analyzer",
        description="Analyze a log file and summarize ERROR/WARNING/INFO counts.",
    )
    parser.add_argument(
        "file",
        type=Path,
        help="Path to the log file (e.g., data/log.txt)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output the results as JSON instead of text",
    )
    return parser


def _format_text_report(counts: Dict[str, int]) -> str:
    total = sum(counts.values())
    lines = ["Log Level Summary:"]
    for level in LOG_LEVELS:
        if level in counts:
            lines.append(f"  {level}: {counts[level]}")
    lines.append(f"  TOTAL: {total}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    counts = count_log_levels(args.file)

    if args.json:
        print(json.dumps(counts, indent=2))
    else:
        print(_format_text_report(counts))

    return 0