import pytest
from um import count
def test_case():
    assert count("Um") == 1
    assert count("um") == 1

def test_in_word():
    assert count("album") == 0
    assert count("umbrella") == 0
    assert count("dummy") == 0

def test_count():
    assert count("Um, I don't know") == 1
    assert count("You, um, said he lost his umbrella") == 1
    assert count("Um, I, um, do not") == 2
