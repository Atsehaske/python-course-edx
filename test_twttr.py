import twttr

def main():
    ''' main function '''

''' tests '''
def test_lowercase():
    assert twttr.shorten('monster') == shorten('monster')
    assert twttr.shorten('velvet') == shorten('velvet')

def test_uppercase():
    assert twttr.shorten('MONSTER') == shorten('MONSTER')
    assert twttr.shorten('VELVET') == shorten('VELVET')

def test_numbers():
    assert twttr.shorten('CS50') == shorten('CS50')
    assert twttr.shorten('jp2') == shorten('jp2')

def test_punctuation():
    assert twttr.shorten('Hey, wassup?') == shorten('Hey, wassup?')
    assert twttr.shorten('Hi!') == shorten('Hi!')


def shorten(word):
    """
    omit vowels
    >>>shorten("TWITTER")
    TWTTR
    >>>shorten("twitter")
    twttr
    """
    vowels = set('AEIOUaeiou')
    return ''.join(c for c in word if c not in vowels)


if __name__ == "__main__":
    main()
