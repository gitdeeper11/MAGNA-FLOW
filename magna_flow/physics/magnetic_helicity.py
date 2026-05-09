"""
Magnetic helicity conservation for MHD systems.
Pure Python implementation.

Equation: H_m = ∫_V (A · B) dV
Equation: dH_m/dt = −2η · ∫_V (J · B) dV
"""

import math
from typing import List, Tuple


class MagneticHelicity:
    """
    Magnetic helicity integrator and conservation enforcer.
    
    H_m = ∫_V (A · B) dV
    dH_m/dt = −2η · ∫_V (J · B) dV
    """
    
    def __init__(self, eta: float = 1e-6):
        self.eta = eta
    
    def compute_helicity(self, bx: List[float], by: List[float], bz: List[float],
                          ax: List[float], ay: List[float], az: List[float]) -> float:
        """Compute magnetic helicity H_m = ∫(A·B)dV."""
        if not bx:
            return 0.0
        
        n = len(bx)
        helicity = 0.0
        for i in range(min(n, len(ax))):
            helicity += ax[i]*bx[i] + ay[i]*by[i] + az[i]*bz[i]
        
        return helicity / n if n > 0 else 0.0
    
    def compute_current_helicity(self, jx: List[float], jy: List[float], jz: List[float],
                                  bx: List[float], by: List[float], bz: List[float]) -> float:
        """Compute current helicity ∫(J·B)dV."""
        if not bx:
            return 0.0
        
        n = len(bx)
        current_hel = 0.0
        for i in range(n):
            current_hel += jx[i]*bx[i] + jy[i]*by[i] + jz[i]*bz[i]
        
        return current_hel / n if n > 0 else 0.0
    
    def helicity_evolution(self, helicity: float, current_helicity: float, dt: float) -> float:
        """Compute helicity evolution: dH_m/dt = −2η·∫(J·B)dV"""
        dHdt = -2.0 * self.eta * current_helicity
        return helicity + dHdt * dt
    
    def helicity_conservation_error(self, helicity_initial: float, helicity_final: float) -> float:
        """Compute relative helicity conservation error."""
        if abs(helicity_initial) < 1e-12:
            return 0.0
        return abs(helicity_final - helicity_initial) / abs(helicity_initial)
