PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
PIP_FLAGS ?= --break-system-packages

.PHONY: install test run clean

install:
	$(PIP) install $(PIP_FLAGS) -e .
	$(PIP) install $(PIP_FLAGS) -r requirements-dev.txt

test:
	$(PYTHON) -m pytest -q

run:
	$(PYTHON) -m log_analyzer data/log.txt

clean:
	rm -rf build dist .eggs *.egg-info .pytest_cache __pycache__