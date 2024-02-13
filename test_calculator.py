from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5, "Addition method failed"

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2, "Subtraction method failed"

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6, "Multiplication method failed"

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 3) == 2, "Division method failed"
    try:
        calc.divide(5, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError:
        pass  # Expected exception

def test_modulo():
    calc = Calculator()
    assert calc.modulo(5, 2) == 1, "Modulo method failed"
    try:
        calc.modulo(5, 0)
        assert False, "Expected ValueError for modulo by zero"
    except ValueError:
        pass  # Expected exception

def test_power():
    calc = Calculator()
    assert calc.power(2, 3) == 8, "Power method failed"

def test_square_root():
    calc = Calculator()
    assert abs(calc.square_root(4) - 2) < 1e-9, "Square root method failed"
    try:
        calc.square_root(-1)
        assert False, "Expected ValueError for square root of negative number"
    except ValueError:
        pass  # Expected exception

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_modulo()
    test_power()
    test_square_root()
    print("All tests passed!")