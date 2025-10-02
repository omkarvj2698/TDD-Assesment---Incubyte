from calculator import Calculator

def test_two_numbers_are_summed():
    calc = Calculator()
    assert calc.add("1,5") == 6