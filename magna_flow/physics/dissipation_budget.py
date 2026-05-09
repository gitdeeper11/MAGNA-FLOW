"""
MHD entropy production rate and dissipation budget.
Pure Python implementation.

Equation: dS/dt = (1/T)·∫_V [ η|J|² + ν|e_ij|² ] dV
"""

import math
from typing import List, Tuple


class DissipationBudget:
    """
    MHD entropy production calculator.
    
    σ_Ohm = η|J|²
    σ_visc = ν|e_ij|²
    dS/dt = (1/T)·∫_V (σ_Ohm + σ_visc) dV
    """
    
    def __init__(self, eta: float = 1e-6, nu: float = 1e-6, temperature: float = 300.0):
        self.eta = eta
        self.nu = nu
        self.temperature = temperature
    
    def ohmic_dissipation(self, jx: List[float], jy: List[float], jz: List[float]) -> float:
        """Compute Ohmic dissipation σ_Ohm = η|J|²."""
        if not jx:
            return 0.0
        
        n = len(jx)
        sigma_ohm = 0.0
        for i in range(n):
            j2 = jx[i]*jx[i] + jy[i]*jy[i] + jz[i]*jz[i]
            sigma_ohm += self.eta * j2
        
        return sigma_ohm / n if n > 0 else 0.0
    
    def viscous_dissipation(self, grad_ux: List[float], grad_uy: List[float], grad_uz: List[float]) -> float:
        """Compute viscous dissipation σ_visc = ν|e_ij|²."""
        # Simplified: e_ij ≈ gradient magnitude
        if not grad_ux:
            return 0.0
        
        n = len(grad_ux)
        sigma_visc = 0.0
        for i in range(n):
            e2 = grad_ux[i]*grad_ux[i] + grad_uy[i]*grad_uy[i] + grad_uz[i]*grad_uz[i]
            sigma_visc += self.nu * e2
        
        return sigma_visc / n if n > 0 else 0.0
    
    def total_entropy_production(self, sigma_ohm: float, sigma_visc: float) -> float:
        """Compute total entropy production rate."""
        return (sigma_ohm + sigma_visc) / self.temperature
    
    def efficiency_index(self, sigma_controlled: float, sigma_uncontrolled: float) -> float:
        """Compute MHD efficiency index η_MHD."""
        if sigma_uncontrolled <= 0:
            return 1.0
        return 1.0 - sigma_controlled / sigma_uncontrolled
