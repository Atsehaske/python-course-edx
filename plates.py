import re
import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_two_letters(s):
    if s[0].isdigit():
        return False
    return True

def check_no_characters(s):
    if 2 <= len(s) <= 6:
        return True
    return False

def check_if_num_in_middle(s):
    ns = s[2:len(s):1] # ns[0,4] s2 s3 s4 s5 s6 s[0,6]
    m = re.search(r"\d", ns)
    if m:
        if ns[m.start()] == '0':
            return False
    for c in range (len(ns)-1, 0, -1):
        if ns[c].isalpha() and ns[c-1:0:-1].isdigit():
            return False
    return True

def check_characters(s):
    for c in s:
        if c in string.punctuation:
            return False
        if c == " ":
            return False
    return True

def is_valid(s):
    if check_characters(s) == False:
        return False
    if is_two_letters(s) == False:
        return False
    if check_no_characters(s) == False:
        return False
    if check_if_num_in_middle(s) == False:
        return False
    return True

main()
