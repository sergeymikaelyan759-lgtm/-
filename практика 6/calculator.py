"""
Calculator class with basic and advanced arithmetic operations.
"""
import math


class Calculator:
    """A comprehensive calculator class for arithmetic operations."""
    
    def __init__(self):
        """Initialize calculator with default value."""
        self.result = 0.0
        self.history = []
    
    def add(self, a, b):
        if a is None or b is None:
            raise ValueError("Arguments cannot be None")
        self.result = float(a) + float(b)
        self.history.append("{} + {} = {}".format(a, b, self.result))
        return self.result
    
    def subtract(self, a, b):
        if a is None or b is None:
            raise ValueError("Arguments cannot be None")
        self.result = float(a) - float(b)
        self.history.append("{} - {} = {}".format(a, b, self.result))
        return self.result
    
    def multiply(self, a, b):
        if a is None or b is None:
            raise ValueError("Arguments cannot be None")
        self.result = float(a) * float(b)
        self.history.append("{} * {} = {}".format(a, b, self.result))
        return self.result
    
    def divide(self, a, b):
        if a is None or b is None:
            raise ValueError("Arguments cannot be None")
        if float(b) == 0:
            raise ValueError("Division by zero is not allowed")
        self.result = float(a) / float(b)
        self.history.append("{} / {} = {}".format(a, b, self.result))
        return self.result
    
    def power(self, base, exponent):
        if base is None or exponent is None:
            raise ValueError("Arguments cannot be None")
        self.result = math.pow(float(base), float(exponent))
        self.history.append("{}^{} = {}".format(base, exponent, self.result))
        return self.result
    
    def square_root(self, number):
        if number is None:
            raise ValueError("Argument cannot be None")
        if float(number) < 0:
            raise ValueError("Cannot calculate square root of negative number")
        self.result = math.sqrt(float(number))
        self.history.append("sqrt({}) = {}".format(number, self.result))
        return self.result
    
    def modulo(self, a, b):
        if a is None or b is None:
            raise ValueError("Arguments cannot be None")
        if float(b) == 0:
            raise ValueError("Modulo by zero is not allowed")
        self.result = float(a) % float(b)
        self.history.append("{} % {} = {}".format(a, b, self.result))
        return self.result
    
    def factorial(self, n):
        if n is None:
            raise ValueError("Argument cannot be None")
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial is only defined for non-negative integers")
        self.result = math.factorial(n)
        self.history.append("{}! = {}".format(n, self.result))
        return self.result
    
    def get_result(self):
        return self.result
    
    def get_history(self):
        return self.history.copy()
    
    def clear_history(self):
        self.history = []
    
    def reset(self):
        self.result = 0.0
        self.history = []
