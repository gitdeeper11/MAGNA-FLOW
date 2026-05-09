import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from magna_flow import MHDStateTracker


class TestTracker(unittest.TestCase):
    
    def test_initialization(self):
        tracker = MHDStateTracker()
        self.assertEqual(tracker.spatial_dim, 256)
        self.assertEqual(tracker.k_max, 64)
    
    def test_initialize_uniform(self):
        tracker = MHDStateTracker()
        tracker.initialize_uniform(u0=0.5, b0=1.0, n_points=100)
        self.assertEqual(len(tracker.ux), 100)
        self.assertEqual(len(tracker.bx), 100)
    
    def test_step(self):
        tracker = MHDStateTracker()
        tracker.initialize_uniform(n_points=10)
        tracker.step(dt=0.01)
        self.assertIsNotNone(tracker.ux)
    
    def test_get_efficiency_index(self):
        tracker = MHDStateTracker()
        eta = tracker.get_efficiency_index()
        self.assertGreaterEqual(eta, 0)
        self.assertLessEqual(eta, 1)
    
    def test_compute_eta_mhd(self):
        tracker = MHDStateTracker()
        eta = tracker.compute_eta_mhd()
        self.assertGreaterEqual(eta, 0)
        self.assertLessEqual(eta, 1)


if __name__ == '__main__':
    unittest.main()
