import sys
import csv
from tabulate import tabulate

def main():
    ''' main function '''
    check_arg()
    open_file()

def check_arg():
    ''' checks if number of args is correct '''
    try:
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            raise Exception
        if len(sys.argv) <= 1:
            print("Too few command-line arguments")
            raise Exception
        if not sys.argv[1].endswith('.csv'):
            print("Not a CSV file")
            raise Exception
    except Exception:
        sys.exit(1)

def open_file():
    ''' opens csv file '''
    try:
        with open(sys.argv[1], newline='') as csvfile:
            # content of menu
            menureader = csv.reader(csvfile, delimiter=",")
            # headers of menu
            headers = next(menureader)
            print(tabulate(menureader, headers, tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
