import re
import sys

def main():
    ''' main function '''
    print(count(input("Text: ")))

def count(s):
    ''' returns occurrences of "um" in string '''
    counter = re.findall(r'\b[U|u]m\b', s.strip())
    return len(counter)

if __name__ == "__main__":
    main()
