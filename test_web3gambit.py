# test_web3gambit.py
"""
Tests for Web3Gambit module.
"""

import unittest
from web3gambit import Web3Gambit

class TestWeb3Gambit(unittest.TestCase):
    """Test cases for Web3Gambit class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Gambit()
        self.assertIsInstance(instance, Web3Gambit)

    def test_run_method(self):
        """Test the run method."""
        instance = Web3Gambit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
