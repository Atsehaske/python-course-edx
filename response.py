import validators

def main():
    ''' main function '''
    print(response(input("What's your email address? ")))

def response(s):
    if validators.email(s.strip()):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
