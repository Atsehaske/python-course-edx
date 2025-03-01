from numb3rs import validate
def main():
    ''' main function '''
    test_numb3r()

def test_numb3r():
    assert validate("10.0.0.10") == True
    assert validate("275.0.0.0") == False
    assert validate("cat") == False
    assert validate("a.a.a.a") == False
    assert validate("1.1.1.1.1.1") == False
    assert validate("10.400.0.0") == False

if __name__ == "__main__":
    main()
