from src.calculator import Calculator

def test_empty_string_returns_0():
    calc = Calculator()
    assert calc.add("") == 0
