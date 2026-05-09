# Contributing to MAGNA-FLOW (E-LAB-09)

Thank you for your interest in contributing to **MAGNA-FLOW**!

## How to Contribute

### 1. Report Bugs
- Use GitHub/GitLab Issues
- Include: Python version, OS, MHD regime, steps to reproduce
- Label: `bug`

### 2. Suggest Features
- Open an issue with label `enhancement`
- Describe the use case and expected behavior
- New MHD regimes are welcome

### 3. Submit Code Changes

#### Prerequisites
```bash
pip install -e .[dev]
pre-commit install
```

Development Workflow

```bash
git clone https://github.com/YOUR_USERNAME/MAGNA-FLOW
cd MAGNA-FLOW
git checkout -b feature/your-feature-name
pytest tests/ -v
git commit -m "feat: add MHD regime"
git push origin feature/your-feature-name
```

4. Update Documentation

· Edit README.md, docs/, or docstrings
· Ensure make docs builds successfully

Code Style

· Python: PEP 8 (use black)
· Type hints: Required for all public functions
· Docstrings: Google style

Testing Requirements

· All tests must pass: pytest tests/ -v
· Coverage should not decrease: pytest --cov=magna_flow
· New features require tests
· Physical constraints (div B = 0, helicity) must be enforced

Commit Convention

Type Description
feat New feature
fix Bug fix
docs Documentation
test Testing
refactor Code refactor
perf Performance improvement

Questions?

Open an issue or email: gitdeeper@gmail.com

---

Thank you for contributing to neural MHD dissipation control! ⚡
