from datetime import date
import re
import sys
import inflect

def main():
    ''' main function '''
    print(seasons(input("Date of Birth: ")))

def time_between(today, birthday):
    ''' returns time between now and birthdate'''
    return abs(today-birthday)

def minutes_in_words(d):
    ''' returns minutes in words'''
    p = inflect.engine()
    return p.number_to_words(d, andword="").capitalize()

def seasons(s):
    ''' returns time that passed since now and date of birth in written minutes
    >>>1999-01-01
    Five houndred twenty five thousand, six hundred minutes
    '''
    if birthday := re.search(r'(\d{4})-(\d{2})-(\d{2})',s):
        year, month, day = int(birthday.group(1)), int(birthday.group(2)), int(birthday.group(3))
        if month > 12 or day > 32:
            print("Invalid date")
            sys.exit(1)
    else:
        print("Invalid date")
        sys.exit(1)
    today = date.today()
    birth = date(year, month, day)
    diff = (time_between(today, birth).days)*24*60
    minutes = minutes_in_words(diff)
    return minutes+' minutes'


if __name__ == "__main__":
    main()
