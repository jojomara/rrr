
# Following Test-Driven Development (TDD) approach

def fibonacci(n):
    """
    Returns the n-th Fibonacci number.
    The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Iterative approach for better efficiency
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Test cases using unittest (following TDD process)
import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(3), 2)

    def test_fibonacci_4(self):
        self.assertEqual(fibonacci(4), 3)

    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_6(self):
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 55)

# This ensures that the tests run when you run the script
if __name__ == '__main__':
    unittest.main()
