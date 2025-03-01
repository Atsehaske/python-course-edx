import re
import sys

def main():
    ''' main '''
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.search(pattern, ip):
        print("Valid")
        return True
    else:
        print("Invalid")
        return False

if __name__ == "__main__":
    main()
