# fibonacci_test.py

from fibonacci import fibonacci  # Importing the fibonacci function

def run_tests():
    print("Running tests for fibonacci...")

    # Test cases
    assert fibonacci(0) == 0, "Test Case 1 Failed: fibonacci(0)"
    assert fibonacci(1) == 1, "Test Case 2 Failed: fibonacci(1)"
    assert fibonacci(2) == 1, "Test Case 3 Failed: fibonacci(2)"
    assert fibonacci(3) == 2, "Test Case 4 Failed: fibonacci(3)"
    assert fibonacci(5) == 5, "Test Case 5 Failed: fibonacci(5)"
    assert fibonacci(10) == 55, "Test Case 6 Failed: fibonacci(10)"
    
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
