import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from magna_flow import MagneticFourierNeuralOperator


class TestMFNO(unittest.TestCase):
    
    def test_initialization(self):
        mfno = MagneticFourierNeuralOperator()
        self.assertEqual(mfno.n_layers, 8)
        self.assertEqual(mfno.k_max, 64)
    
    def test_forward_pass(self):
        mfno = MagneticFourierNeuralOperator()
        ux = [0.1, 0.2, 0.3]
        uy = [0.1, 0.2, 0.3]
        uz = [0.1, 0.2, 0.3]
        bx = [1.0, 1.0, 1.0]
        by = [1.0, 1.0, 1.0]
        bz = [1.0, 1.0, 1.0]
        
        result = mfno.forward(ux, uy, uz, bx, by, bz)
        self.assertEqual(len(result), 6)
    
    def test_spectral_kernel(self):
        mfno = MagneticFourierNeuralOperator()
        kernel = mfno.spectral_kernel(k=1)
        self.assertEqual(len(kernel), 6)
        self.assertEqual(len(kernel[0]), 6)


if __name__ == '__main__':
    unittest.main()
