# test_safepallink.py
"""
Tests for SafePalLink module.
"""

import unittest
from safepallink import SafePalLink

class TestSafePalLink(unittest.TestCase):
    """Test cases for SafePalLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SafePalLink()
        self.assertIsInstance(instance, SafePalLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SafePalLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
