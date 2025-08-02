# test_nanospectral.py
"""
Tests for NanoSpectral module.
"""

import unittest
from nanospectral import NanoSpectral

class TestNanoSpectral(unittest.TestCase):
    """Test cases for NanoSpectral class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NanoSpectral()
        self.assertIsInstance(instance, NanoSpectral)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NanoSpectral()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
