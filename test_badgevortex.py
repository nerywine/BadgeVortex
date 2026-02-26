# test_badgevortex.py
"""
Tests for BadgeVortex module.
"""

import unittest
from badgevortex import BadgeVortex

class TestBadgeVortex(unittest.TestCase):
    """Test cases for BadgeVortex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BadgeVortex()
        self.assertIsInstance(instance, BadgeVortex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BadgeVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
