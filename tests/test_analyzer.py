from pathlib import Path

from log_analyzer.analyzer import count_log_levels, extract_level_from_line


def test_extract_level_from_line_matches_valid_patterns():
    assert extract_level_from_line("[2025-08-10 10:00:00] ERROR: Failure") == "ERROR"
    assert extract_level_from_line("[2025-08-10 10:00:00] WARNING: Check this") == "WARNING"
    assert extract_level_from_line("[2025-08-10 10:00:00] INFO: Hello") == "INFO"


def test_extract_level_from_line_ignores_non_matching_lines():
    assert extract_level_from_line("No timestamp here") is None
    assert extract_level_from_line("[2025] DEBUG: Not counted") is None
    assert extract_level_from_line("[2025-08-10] ERROR no colon") is None


def test_count_log_levels_counts_levels_correctly(tmp_path: Path):
    content = "\n".join(
        [
            "[2025-08-10 10:00:00] ERROR: First error",
            "[2025-08-10 10:01:00] WARNING: Something odd",
            "[2025-08-10 10:02:00] INFO: Just an info",
            "[2025-08-10 10:03:00] ERROR: Second error",
            "[2025-08-10 10:04:00] INFO: Another info",
            "gibberish line that should be ignored",
            "[2025-08-10 10:05:00] DEBUG: Ignored level",
        ]
    )
    log_file = tmp_path / "test.log"
    log_file.write_text(content, encoding="utf-8")

    counts = count_log_levels(log_file)
    assert counts["ERROR"] == 2
    assert counts["WARNING"] == 1
    assert counts["INFO"] == 2