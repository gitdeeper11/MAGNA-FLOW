"""
MAGNA-FLOW (E-LAB-09)
Neural Magnetohydrodynamic Dissipation Control for High-Conductivity Turbulent Plasma Systems

Author: Samir Baladi
DOI: 10.5281/zenodo.19893462
License: MIT
"""

from .version import __version__, __doi__, __author__

__all__ = [
    "__version__",
    "__doi__",
    "__author__",
    "MHDStateTracker",
    "MagnaFlowEngine",
    "MagneticFourierNeuralOperator",
    "HydromagneticPINN",
    "LorentzFluxResolver",
]

from .tracker.mhd_state_tracker import MHDStateTracker
from .interface.magna_flow_engine import MagnaFlowEngine
from .neural.mfno import MagneticFourierNeuralOperator
from .neural.hpinn import HydromagneticPINN
from .control.lflux_resolver import LorentzFluxResolver
