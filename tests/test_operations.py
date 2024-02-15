from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


def test_operation_add():
    calculation : Decimal= Calculation(Decimal('10'), Decimal('5'), add)
    assert calculation.perform() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    calculation : Decimal = Calculation(Decimal('10'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('5'), "Subtract operation failed"

def test_operation_multiply():
    calculation : Decimal = Calculation(Decimal('10'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('50'), "Multiply operation failed"

def test_operation_divide():
    calculation : Decimal = Calculation(Decimal('10'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        calculation : Decimal = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
