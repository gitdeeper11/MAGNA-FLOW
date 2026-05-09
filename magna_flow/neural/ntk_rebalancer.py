"""
Neural Tangent Kernel (NTK) loss rebalancer for H-PINN.
Dynamically adjusts loss weights to balance gradient magnitudes.
"""

from typing import List, Dict
import math


class NTKRebalancer:
    """
    NTK-based loss weight rebalancing.
    
    Updates λ_i every N epochs to prevent any single physics constraint
    from dominating the gradient signal.
    """
    
    def __init__(self, n_losses: int = 4, update_interval: int = 250):
        self.n_losses = n_losses
        self.update_interval = update_interval
        self.weights = [1.0, 8.0, 12.0, 4.0]  # λ₁, λ₂, λ₃, λ₄
        self.gradient_norms = [[] for _ in range(n_losses)]
    
    def update(self, gradients: List[float], epoch: int) -> List[float]:
        """Update loss weights based on gradient norms."""
        # Record gradient norms
        for i, g in enumerate(gradients):
            self.gradient_norms[i].append(abs(g))
        
        # Update weights every update_interval epochs
        if epoch % self.update_interval == 0 and epoch > 0:
            means = [sum(norms[-self.update_interval:]) / len(norms[-self.update_interval:]) 
                    for norms in self.gradient_norms if norms]
            
            if means and min(means) > 0:
                target = max(means)
                new_weights = [target / m for m in means]
                # Normalize to keep scale
                self.weights = [w / sum(new_weights) * sum(self.weights) for w in new_weights]
        
        return self.weights
    
    def get_weights(self) -> List[float]:
        """Return current loss weights."""
        return self.weights
