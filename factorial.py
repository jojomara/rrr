def factorial(n):
    """
    Calculates the factorial of a given number.
    
    :param n: A non-negative integer.
    :return: Factorial of the number, or None for negative numbers.
    """
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    if n == 0:
        return 1  # Base case: 0! is 1
    return n * factorial(n - 1)  # Recursive case


# Tests for the factorial function
def run_tests():
    print("Running tests for factorial...")

    # Test cases
    assert factorial(0) == 1, "Test Case 1 Failed: factorial(0)"
    assert factorial(1) == 1, "Test Case 2 Failed: factorial(1)"
    assert factorial(5) == 120, "Test Case 3 Failed: factorial(5)"
    assert factorial(-1) == None, "Test Case 4 Failed: factorial(-1)"
    
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
