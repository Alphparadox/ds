import math

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

def calculator(operator, num1, num2):
    """Performs basic arithmetic operations."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero."
        return num1 / num2
    else:
        return "Error: Invalid operator."

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_series(limit):
    """Generates the Fibonacci series up to a given limit."""
    series = []
    a, b = 0, 1
    while a <= limit:
        series.append(a)
        a, b = b, a + b
    return series

def find_max(arr):
    """Finds the maximum value in a list of numbers."""
    if not arr:
        return "Error: The list is empty."
    return max(arr)