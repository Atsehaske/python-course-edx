import sys

def main():
    ''' main function '''
    check_args()
    print(count_lines())

def check_args():
    """ check if no of arg is correct along with corrent file format """
    if len(sys.argv) < 2 :
        print("Too few command-line arguments")
        sys.exit(1)
    try:
        if len(sys.argv) > 2 :
            raise Exception
    except Exception:
        print("Too many command-line arguments")
        sys.exit(1)
    for arg in sys.argv:
        if arg.endswith('.txt'):
            print("Not a Python file")
            sys.exit(1)

def count_lines():
    ''' count lines in file excluding blanks and lines starting with #'''
    count = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.lstrip()
                if line and not line.startswith('#'):
                    count = count + 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    return count

if __name__ == "__main__":
    main()
