import bank

def main():
    ''' main function '''

def value(greeting):
    return bank.value(greeting)

def test_hello():
    tests = ['hello', 'Hello']
    for i in tests:
        assert value(i) == 0

def test_first_h():
    tests = ['hey', 'hi']
    for i in tests:
        assert value(i) == 20

def test_not_h_or_hello():
    tests = ['Whats up?', 'yo']
    for i in tests:
        assert value(i) == 100


if __name__ == "__main__":
    main()
