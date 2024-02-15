from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

# Definition of the Calculation class with type annotations for improved readability and safety
class Calculation:
    # Constructor method
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        # Store the operation as callable
        self.operation = operation
    
    # Static method to create a new instance of Calculation
    # alternative constructor to instantiate object through indirect reference
    @staticmethod    
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        # Return a new Calculation object initialized with the provided arguments
        return Calculation(a, b, operation)

    # perform calculation stored in object
    def perform(self) -> Decimal:
        return self.operation(self.a, self.b)

    # Special method to provide a string representation of the Calculation instance
    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
