"""
Loss functions for M-FNO and H-PINN training.
"""

import math
from typing import List, Tuple


class MSELoss:
    """Mean squared error loss."""
    
    def __call__(self, pred: List[float], target: List[float]) -> float:
        if not pred:
            return 0.0
        n = len(pred)
        loss = sum((pred[i] - target[i])**2 for i in range(min(n, len(target))))
        return loss / n


class PhysicsLoss:
    """Physics-informed loss components."""
    
    def momentum_loss(self, du_dt: List[float], u: List[float], du_dx: List[float],
                      b: List[float], db_dx: List[float]) -> float:
        """Momentum equation residual."""
        if not du_dt:
            return 0.0
        n = len(du_dt)
        loss = 0.0
        for i in range(n):
            residual = du_dt[i] + u[i]*du_dx[i] - b[i]*db_dx[i]
            loss += residual**2
        return loss / n
    
    def induction_loss(self, db_dt: List[float], u: List[float], db_dx: List[float],
                       b: List[float], du_dx: List[float]) -> float:
        """Induction equation residual."""
        if not db_dt:
            return 0.0
        n = len(db_dt)
        loss = 0.0
        for i in range(n):
            residual = db_dt[i] - (u[i]*db_dx[i] - b[i]*du_dx[i])
            loss += residual**2
        return loss / n
    
    def divergence_loss(self, dux_dx: List[float], duy_dy: List[float], duz_dz: List[float],
                        dbx_dx: List[float], dby_dy: List[float], dbz_dz: List[float]) -> float:
        """Divergence penalty."""
        n = len(dux_dx) if dux_dx else 0
        if n == 0:
            return 0.0
        loss_u = 0.0
        loss_b = 0.0
        for i in range(n):
            loss_u += (dux_dx[i] + duy_dy[i] + duz_dz[i])**2
            loss_b += (dbx_dx[i] + dby_dy[i] + dbz_dz[i])**2
        return (loss_u + loss_b) / n
    
    def helicity_loss(self, helicity: float, target_helicity: float = 0.0) -> float:
        """Helicity conservation loss."""
        return (helicity - target_helicity) ** 2
