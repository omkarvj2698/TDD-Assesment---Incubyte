from calculator import Calculator

def test_single_number_returns_value():
    calc = Calculator()
    assert calc.add("7") == 7
