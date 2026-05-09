"""Calculator entry point."""
from calculator import Calculator


def run_calculator():
    """Calculator entry point."""
    number1 = int(input("enter the first number::>"))
    number2 = int(input("enter the second number::>"))

    calc1 = Calculator(number1, number2)
    calc1.calculate()

run_calculator()