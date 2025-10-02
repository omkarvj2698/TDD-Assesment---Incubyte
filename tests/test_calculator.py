from calculator import Calculator
import pytest

def test_placeholder():
    calc = Calculator()
    assert isinstance(calc, Calculator)

def test_empty_string_returns_0():
    calc = Calculator()
    assert calc.add("") == 0

def test_single_number_returns_value():
    calc = Calculator()
    assert calc.add("7") == 7

def test_two_numbers_are_summed():
    calc = Calculator()
    assert calc.add("1,5") == 6

def test_newline_as_delimiter():
    calc = Calculator()
    assert calc.add("1\n2,3") == 6

def test_custom_delimiter_header_semicolon():
    calc = Calculator()
    assert calc.add("//;\n1;2;3") == 6

def test_negatives_raise_listing_all():
    calc = Calculator()
    with pytest.raises(ValueError) as exc:
        calc.add("1,-2,3,-5")
    assert str(exc.value) == "negative numbers not allowed -2,-5"

def test_custom_delimiter_bracket_form_single_char():
    calc = Calculator()
    assert calc.add("//[;]\n1;2;3") == 6