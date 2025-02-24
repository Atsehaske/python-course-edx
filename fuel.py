def main():
    fuel = get_int()
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(str("%.0f" % fuel)+"%")

def get_int():
    while True:
        try:
            x, y = list(map(int,input("Fraction: ").split("/")))
            if x > y:
                raise ValueError
            return (x/y)*100
        except (ValueError, ZeroDivisionError):
            pass


main()
