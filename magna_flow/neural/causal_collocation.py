"""
Causal collocation point sampler for time-dependent PINNs.
Ensures causality by weighting earlier times more heavily.
"""

import math
from typing import List, Tuple
import random


class CausalCollocation:
    """
    Causal collocation point sampling with exponential annealing.
    
    Equation: w(t_k) = exp(-ε · Σ_{i<k} L_phys(t_i))
    """
    
    def __init__(self, epsilon: float = 0.1, n_points: int = 4096):
        self.epsilon = epsilon
        self.n_points = n_points
        self.causal_weights: List[float] = []
        self.prior_residuals: List[float] = []
    
    def compute_weight(self, time_index: int, prior_residuals: List[float]) -> float:
        """Compute causal weight w(t_k)."""
        if not prior_residuals:
            return 1.0
        cum_sum = sum(prior_residuals[:time_index])
        return math.exp(-self.epsilon * cum_sum)
    
    def sample_points(self, n_times: int, n_spatial: int) -> List[Tuple[float, float, float]]:
        """Sample collocation points in spatiotemporal domain."""
        points = []
        for _ in range(self.n_points):
            t = random.uniform(0, 1)
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            points.append((t, x, y))
        return points
    
    def get_causal_weights(self, residuals: List[float]) -> List[float]:
        """Compute causal weights for all time steps."""
        weights = []
        for i, res in enumerate(residuals):
            w = self.compute_weight(i, residuals[:i])
            weights.append(w)
        return weights
