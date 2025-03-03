import pytest
from jar import Jar
import emoji

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == emoji.emojize(':cookie:',language='alias')
    jar.deposit(1)
    assert str(jar) == (emoji.emojize(':cookie:',language='alias')+emoji.emojize(':cookie:',language='alias'))

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5
    with pytest.raises(ValueError):
        assert jar.deposit(20)

def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        assert jar.withdraw(20)
