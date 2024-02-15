from calculator.calculations import Calculations  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide 
from calculator.calculation import Calculation  
from decimal import Decimal  
from typing import Callable  

# Definition of the Calculator class
class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        # add to calculation history
        Calculations.add_calculation(calculation)
        return calculation.perform()

    #add, subtract, multiply, and divide operations
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, add)


    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, subtract)


    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, multiply)

 
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, divide)
