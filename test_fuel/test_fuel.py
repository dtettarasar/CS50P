from fuel import convert, gauge
import pytest

def test_convert_valid_format():
    assert convert("1/2") == 50

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        assert convert("cat/dog")
        assert convert("cat")

def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        assert convert("12/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(45) == "45%"
