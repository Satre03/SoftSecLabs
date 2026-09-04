from src.calculator import Calculator

def test_calc():
    calculator = Calculator()

    # Test addition
    assert calculator.calc("2 + 3") == "5"

    # Test subtraction
    assert calculator.calc("10 - 4") == "6"

    # Test multiplication
    assert calculator.calc("3 * 5") == "15"

    # Test division
    assert calculator.calc("20 / 4") == "5.0"

    # Test parentheses
    assert calculator.calc("(2 + 3) * 4") == "20"

    # Test exponentiation
    assert calculator.calc("2 ** 3") == "8"

    # Test complex expression
    assert calculator.calc("2 + 3 * (4 - 1)") == "11"