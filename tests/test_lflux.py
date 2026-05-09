import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from magna_flow import LorentzFluxResolver


class TestLFlux(unittest.TestCase):
    
    def test_initialization(self):
        lflux = LorentzFluxResolver()
        self.assertEqual(lflux.horizon_us, 500)
        self.assertEqual(lflux.b_max, 1.2)
    
    def test_compute_control(self):
        lflux = LorentzFluxResolver()
        
        # Safe condition
        control = lflux.compute_control(lambda_min=0.2, dlambda_dt=0)
        self.assertEqual(control, 0.0)
        
        # Warning condition
        control = lflux.compute_control(lambda_min=0.06, dlambda_dt=0)
        self.assertGreater(control, 0)
        
        # Critical condition
        control = lflux.compute_control(lambda_min=0.01, dlambda_dt=0)
        self.assertEqual(control, 1.2)
    
    def test_safety_margin(self):
        lflux = LorentzFluxResolver()
        margin = lflux.safety_margin(0.1)
        self.assertEqual(margin, 0.05)


if __name__ == '__main__':
    unittest.main()
