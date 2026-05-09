
MAGNA-FLOW (E-LAB-09) Makefile

.PHONY: install test clean build deploy docs help

help:
@echo "MAGNA-FLOW (E-LAB-09) Commands:"
@echo "  make install   - Install package"
@echo "  make test      - Run unit tests"
@echo "  make coverage  - Run tests with coverage"
@echo "  make clean     - Remove build artifacts"
@echo "  make build     - Build PyPI package"
@echo "  make deploy    - Upload to PyPI"
@echo "  make format    - Format code with black"
@echo "  make run       - Run MHD control simulation"

install:
pip install -e .[dev]
pre-commit install

test:
pytest tests/ -v

coverage:
pytest tests/ -v --cov=magna_flow --cov-report=html

clean:
rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .coverage htmlcov/
find . -type d -name pycache -exec rm -rf {} + 2>/dev/null || true

build: clean
python -m build

deploy:
twine upload dist/*

format:
black magna_flow/ tests/
isort magna_flow/ tests/

run:
python bin/run_control.py --regime tokamak_elm --steps 1000 --verbose

all: clean install test build
