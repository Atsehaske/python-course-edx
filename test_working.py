from working import convert
import pytest

def test_wrong_format():
    with pytest.raises(ValueError):
        assert convert("9 AM - 9 PM")
        assert convert("9 AM 9 PM")

def test_validation():
    with pytest.raises(ValueError):
        assert convert("13 PM to 17 PM")
        assert convert("9:60 AM to 9:60 PM")
        assert convert("15:60 AM to 9:60 PM")

def test_convert_hours():
    assert convert("7:20 AM to 7:10 PM") == "07:20 to 19:10"
    assert convert("7 AM to 7 PM") == "07:00 to 19:00"
    assert convert("7 PM to 9 PM") == "19:00 to 21:00"
    assert convert("7 AM to 8 AM") == "07:00 to 08:00"

def test_convert_minutes():
    assert convert("7:10 AM to 7:13 PM") == "07:10 to 19:13"
    assert convert("7 AM to 7 PM") == "07:00 to 19:00"
