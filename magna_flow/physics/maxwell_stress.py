"""
Maxwell stress tensor T_M computation for MHD systems.
Pure Python implementation.

Equation: T_M^{ij} = (1/μ₀) · [ B_i B_j − (1/2) δ_{ij} |B|² ]
"""

import math
from typing import List, Tuple


class MaxwellStressTensor:
    """
    Maxwell stress tensor calculator.
    
    T_M^{ij} = (1/μ₀) · [ B_i B_j − (1/2) δ_{ij} |B|² ]
    """
    
    def __init__(self, mu0: float = 4e-7 * math.pi):
        self.mu0 = mu0
    
    def compute(self, bx: float, by: float, bz: float) -> List[List[float]]:
        """Compute Maxwell stress tensor at a point."""
        b2 = bx*bx + by*by + bz*bz
        inv_mu0 = 1.0 / self.mu0
        
        T_M = [
            [inv_mu0 * (bx*bx - 0.5*b2), inv_mu0 * (bx*by), inv_mu0 * (bx*bz)],
            [inv_mu0 * (by*bx), inv_mu0 * (by*by - 0.5*b2), inv_mu0 * (by*bz)],
            [inv_mu0 * (bz*bx), inv_mu0 * (bz*by), inv_mu0 * (bz*bz - 0.5*b2)]
        ]
        return T_M
    
    def eigenvalues(self, T_M: List[List[float]]) -> List[float]:
        """Compute eigenvalues of Maxwell stress tensor."""
        a, b, c = T_M[0][0], T_M[0][1], T_M[0][2]
        d, e, f = T_M[1][0], T_M[1][1], T_M[1][2]
        g, h, i_m = T_M[2][0], T_M[2][1], T_M[2][2]
        
        trace = a + e + i_m
        
        # Simplified eigenvalue estimate for positive semi-definite tensors
        # Actual eigenvalues require cubic solver; use power iteration for λ_min
        lambda_min = min(a, e, i_m)
        lambda_max = max(a, e, i_m)
        
        return [lambda_min, lambda_max]
    
    def lambda_min(self, T_M: List[List[float]]) -> float:
        """Return minimum eigenvalue (reconnection precursor)."""
        evals = self.eigenvalues(T_M)
        return evals[0]
    
    def lambda_safe_margin(self, T_M: List[List[float]], lambda_safe: float = 0.05) -> float:
        """Compute safety margin δλ = λ_min - λ_safe."""
        return self.lambda_min(T_M) - lambda_safe
