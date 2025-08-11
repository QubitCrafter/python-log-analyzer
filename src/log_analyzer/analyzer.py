from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, Iterable, Optional


LOG_LEVELS: tuple[str, ...] = ("ERROR", "WARNING", "INFO")

# Matches lines like: [2025-01-02 12:34:56] ERROR: Something happened
_LOG_LINE_PATTERN = re.compile(r"^\s*\[[^\]]+\]\s*(?P<level>ERROR|WARNING|INFO)\s*:\s*(?P<message>.*)$")


def extract_level_from_line(line: str) -> Optional[str]:
    """Return the log level (ERROR/WARNING/INFO) if the line matches the expected pattern.

    Lines that do not match return None.
    """
    match = _LOG_LINE_PATTERN.match(line)
    if not match:
        return None
    return match.group("level")


def count_log_levels(file_path: str | Path, levels: Iterable[str] = LOG_LEVELS) -> Dict[str, int]:
    """Count occurrences of specific log levels in the given file.

    Parameters
    ----------
    file_path: str | Path
        Path to the log file.
    levels: Iterable[str]
        Iterable of level names to count. Defaults to ERROR, WARNING, INFO.

    Returns
    -------
    Dict[str, int]
        Mapping of level name to count.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Log file not found: {path}")

    wanted = {level.upper() for level in levels}
    counts: Dict[str, int] = {level: 0 for level in wanted}

    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            level = extract_level_from_line(line)
            if level and level in wanted:
                counts[level] += 1

    # Ensure deterministic order (helpful for display), though dicts are ordered by insertion in 3.7+
    return {level: counts.get(level, 0) for level in LOG_LEVELS if level in counts}