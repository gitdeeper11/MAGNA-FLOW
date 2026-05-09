"""
Elsässer variable decomposition for MHD.
Equation: z± = u ± B

Represent Alfvén wave packets propagating in opposite directions.
"""

from typing import List, Tuple


class ElsasserDecomp:
    """
    Elsässer variable decomposition.
    
    z⁺ = u + B  (propagating along B)
    z⁻ = u - B  (propagating opposite to B)
    """
    
    def __init__(self):
        pass
    
    def compute_zplus(self, ux: List[float], uy: List[float], uz: List[float],
                     bx: List[float], by: List[float], bz: List[float]) -> Tuple[List[float], List[float], List[float]]:
        """Compute z⁺ = u + B."""
        n = min(len(ux), len(bx)) if ux else 0
        zx = [ux[i] + bx[i] for i in range(n)] if n > 0 else []
        zy = [uy[i] + by[i] for i in range(n)] if n > 0 else []
        zz = [uz[i] + bz[i] for i in range(n)] if n > 0 else []
        return (zx, zy, zz)
    
    def compute_zminus(self, ux: List[float], uy: List[float], uz: List[float],
                      bx: List[float], by: List[float], bz: List[float]) -> Tuple[List[float], List[float], List[float]]:
        """Compute z⁻ = u - B."""
        n = min(len(ux), len(bx)) if ux else 0
        zx = [ux[i] - bx[i] for i in range(n)] if n > 0 else []
        zy = [uy[i] - by[i] for i in range(n)] if n > 0 else []
        zz = [uz[i] - bz[i] for i in range(n)] if n > 0 else []
        return (zx, zy, zz)
    
    def cross_helicity(self, ux: List[float], uy: List[float], uz: List[float],
                       bx: List[float], by: List[float], bz: List[float]) -> float:
        """Compute cross helicity H_c = ∫ (u·B) dV."""
        n = min(len(ux), len(bx)) if ux else 0
        if n == 0:
            return 0.0
        hc = 0.0
        for i in range(n):
            hc += ux[i]*bx[i] + uy[i]*by[i] + uz[i]*bz[i]
        return hc / n
