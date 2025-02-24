import plates

def main():
    ''' main function '''

def is_valid(s):
    ''' run plates is_valid function '''
    '''
    >>> is_valid("CS50")
    True
    '''
    return plates.is_valid(s)

def test_req():
    assert is_valid("AA50") == True
    assert is_valid("CS05") == False
    assert is_valid("AA55P") == False
    assert is_valid("G") == False
    assert is_valid("AAA000") == False
    assert is_valid("AAA222") == True
    assert is_valid("2134A") == False
    assert is_valid("AI3.12") == False
    assert is_valid("2137") == False

if __name__ == "__main__":
    main()
