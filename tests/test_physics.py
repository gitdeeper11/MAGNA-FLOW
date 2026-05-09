import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from magna_flow.physics.maxwell_stress import MaxwellStressTensor
from magna_flow.physics.magnetic_helicity import MagneticHelicity
from magna_flow.physics.dissipation_budget import DissipationBudget


class TestPhysics(unittest.TestCase):
    
    def test_maxwell_stress(self):
        stress = MaxwellStressTensor()
        T_M = stress.compute(bx=1.0, by=0.0, bz=0.0)
        self.assertEqual(len(T_M), 3)
        self.assertEqual(len(T_M[0]), 3)
    
    def test_magnetic_helicity(self):
        helicity = MagneticHelicity()
        h = helicity.compute_helicity([1.0], [0.0], [0.0], [1.0], [0.0], [0.0])
        self.assertGreaterEqual(h, 0)
    
    def test_dissipation_budget(self):
        budget = DissipationBudget()
        sigma_ohm = budget.ohmic_dissipation([1.0], [0.0], [0.0])
        self.assertGreaterEqual(sigma_ohm, 0)
        
        eta = budget.efficiency_index(0.1, 0.942)
        self.assertAlmostEqual(eta, 0.8938, places=3)


if __name__ == '__main__':
    unittest.main()
