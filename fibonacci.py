# fibonacci.py

def fibonacci(n):
    """
    Returns the n-th Fibonacci number.
    
    :param n: A non-negative integer.
    :return: n-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
