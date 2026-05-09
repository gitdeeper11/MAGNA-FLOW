import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from magna_flow import HydromagneticPINN


class TestHPINN(unittest.TestCase):
    
    def test_initialization(self):
        hpinn = HydromagneticPINN()
        self.assertEqual(hpinn.lambda1, 1.0)
        self.assertEqual(hpinn.lambda2, 8.0)
        self.assertEqual(hpinn.lambda3, 12.0)
        self.assertEqual(hpinn.lambda4, 4.0)
    
    def test_total_loss(self):
        hpinn = HydromagneticPINN()
        ux = [0.1, 0.2]
        uy = [0.1, 0.2]
        uz = [0.1, 0.2]
        bx = [1.0, 1.0]
        by = [1.0, 1.0]
        bz = [1.0, 1.0]
        
        loss = hpinn.total_loss(ux, uy, uz, bx, by, bz)
        self.assertGreaterEqual(loss, 0)
    
    def test_onsager_symmetry(self):
        hpinn = HydromagneticPINN()
        L = [[1.0, 2.0], [3.0, 4.0]]
        sym = hpinn.enforce_onsager_symmetry(L)
        self.assertEqual(sym[0][1], sym[1][0])


if __name__ == '__main__':
    unittest.main()
