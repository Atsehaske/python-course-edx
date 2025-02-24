from pyfiglet import Figlet
import random
import sys


def fig():
    figlet = Figlet()
    figfonts = figlet.getFonts()
    try:
        if ("-f" or "--font" or "None") != sys.argv[1] or sys.argv[2] not in figfonts:
            raise SystemExit
        usr_input = input("Input: ")
        if len(sys.argv) == 0:
            figlet.setFont(font=random.choice(figfonts))
        if ("-f" or "--font") == sys.argv[1]:
            figlet.setFont(font=sys.argv[2])
    except SystemExit:
        print("Invalid usage")
        sys.exit(1)
    return figlet.renderText(usr_input)


def main():
    print(fig())

main()
