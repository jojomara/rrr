import unittest
from factorial import factorial  # Import from the file where your factorial function is defined
 # Replace 'your_module' with the actual module name where your factorial function is defined.

class TestFactorial(unittest.TestCase):

    def test_factorial_zero(self):
        """Test factorial of 0"""
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        """Test factorial of 1"""
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive(self):
        """Test factorial of a positive number"""
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative(self):
        """Test factorial of a negative number (should return None)"""
        self.assertIsNone(factorial(-1))

if __name__ == "__main__":
    unittest.main()
