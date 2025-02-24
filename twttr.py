def main():
    ''' main function '''
    user_input = input("Input: ")
    print(shorten(user_input))

def shorten(word):
    '''
    omits all the vowels in given word
    >>>shorten('twitter')
    twttr
    '''
    output = ""
    for letter in word:
        if letter.lower() not in ('a', 'o','e', 'i', 'u'):
            output += letter
   # print("Output: "+output)
    return output

if __name__ == "__main__":
    main()
