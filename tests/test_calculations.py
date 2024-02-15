from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import Calculations


from calculator.operations import add, subtract


@pytest.fixture
def setup_calculations():
    # Clear calculation history
    Calculations.clear_history()

    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    # Create new calculation
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    # Add the calculation to the history.
    Calculations.add_calculation(calc)

    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    # Retrieve the calculation history.
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    # Clear the calculation history.
    Calculations.clear_history()
    # Assert that the history is empty by checking its length.
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    # Retrieve the latest calculation from the history.
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"
