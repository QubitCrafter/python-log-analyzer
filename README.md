# Command-Line Log Analyzer

A simple, production-ready Python tool that reads a log file and summarizes how many `ERROR`, `WARNING`, and `INFO` messages it contains. It is useful for quick analysis of application logs, CI test output, and automation metrics.

## What this project does
- Parses log lines shaped like `[TIMESTAMP] LEVEL: Message`
- Counts occurrences of `ERROR`, `WARNING`, and `INFO`
- Outputs a clean summary (text or JSON)

## Technologies used
- **Python 3.9+**
- **setuptools** for packaging and console script
- **pytest** for tests

## Project structure
```
.
├── data/
│   └── log.txt                 # Sample log file
├── src/
│   └── log_analyzer/
│       ├── __init__.py
│       ├── __main__.py         # Enables `python -m log_analyzer`
│       ├── analyzer.py         # Core parsing/counting logic
│       └── cli.py              # Command-line interface
├── tests/
│   └── test_analyzer.py        # Unit tests (pytest)
├── Makefile                    # install, test, run, clean
├── pyproject.toml              # Packaging configuration
├── requirements-dev.txt        # Dev deps (pytest)
└── README.md
```

## Setup
1. Ensure you have Python 3.9+ installed.
2. Install in editable mode along with dev dependencies:

```bash
make install
```

This installs the package and the `log-analyzer` console command.

## How to run
- Using the console command (after `make install`):

```bash
log-analyzer data/log.txt
```

- Using the module directly:

```bash
python -m log_analyzer data/log.txt
```

- Output as JSON:

```bash
log-analyzer --json data/log.txt
```

## Sample output
```
Log Level Summary:
  ERROR: 2
  WARNING: 2
  INFO: 4
  TOTAL: 8
```

## Log format
The analyzer expects lines like:
```
[2025-08-10 10:00:00] ERROR: Something happened
```
Lines that do not match the pattern are ignored. Only `ERROR`, `WARNING`, and `INFO` are counted.

## Testing
Run unit tests with:
```bash
make test
```

## Notes
- If you want to analyze other levels, extend `LOG_LEVELS` and the regex in `src/log_analyzer/analyzer.py`.
- The tool handles unknown lines gracefully by skipping them.
