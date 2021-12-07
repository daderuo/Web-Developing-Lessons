import unittest
from prime import is_prime

class Test(unittest.TestCase):

    def test_1(self):
        """Check if 1 is not prime."""
        self.assertFalse(is_prime(1))
    
    def test_2(self):
        """Check if 2 is prime."""
        self.assertTrue(is_prime(2))


    def test_8(self):
        """Check if 8 is not prime."""
        self.assertFalse(is_prime(8))

    
    def test_25(self):
        """Check if 25 is not prime."""
        self.assertFalse(is_prime(25))


if __name__ == '__main__':
    unittest.main()