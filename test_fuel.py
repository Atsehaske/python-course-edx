import fuel
import pytest

def main():
    ''' main function '''

def convert(fraction):
    ''' '''
    return fuel.convert(fraction)


def gauge(percentage):
    ''' '''
    return fuel.gauge(percentage)

def test_convert():
    with pytest.raises(Exception) as e_info:
        assert convert("a/A")
        assert convert("1/a")
        assert convert("a/1")
        assert convert("100/20")
    with pytest.raises(ValueError):
        assert convert("three/four")
        assert convert("1.5/3")

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0")

def test_convert_rets():
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(20) == "20%"

if __name__ == "__main__":
    main()
