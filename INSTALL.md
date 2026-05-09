
📦 Installation Guide for MAGNA-FLOW (E-LAB-09)

Quick Install (PyPI)

```bash
pip install magna-flow-engine
```

Install from Source

```bash
git clone https://github.com/gitdeeper11/MAGNA-FLOW.git
cd MAGNA-FLOW
pip install -e .
```

Verify Installation

```python
import magna_flow
print(magna_flow.__version__)  # 1.0.0
print(magna_flow.__doi__)      # 10.5281/zenodo.19893462
```

```bash
python bin/run_control.py --regime tokamak_elm --steps 100 --verbose
```

---

Requirements

Package Version Required
Python ≥ 3.11 ✅ Yes
torch ≥ 2.3.0 ✅ Yes
numpy ≥ 1.24.0 ✅ Yes
scipy ≥ 1.10.0 ✅ Yes
cuFFT (optional) ⚠️ For GPU acceleration

---

Platform Support

Platform Support
Linux ✅ Fully tested
macOS ✅ Compatible
Windows ✅ Compatible
Termux (Android) ✅ Compatible
NVIDIA Jetson Orin ✅ TensorRT supported

---

Docker Installation

```bash
docker pull gitdeeper11/magna-flow:latest
docker run --rm magna-flow --help
```

---

Uninstall

```bash
pip uninstall magna-flow-engine
```

---

For issues, open a ticket on GitHub/GitLab.
