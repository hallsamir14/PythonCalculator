from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        #Add new calcluation to history
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        #Retrieve whole history
        return cls.history

    @classmethod
    def clear_history(cls):
        #Clear calculation history
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        #Get latest calculation.
        if cls.history:
            return cls.history[-1]
        return None


