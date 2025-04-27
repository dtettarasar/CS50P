from working import convert
import pytest

def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

def test_invalid_minute():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5 PM")


def test_valid_input():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert('10:30 PM to 8 AM') == "22:30 to 08:00"


def test_invalid_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("17:00 to 9 PM")
