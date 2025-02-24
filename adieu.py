import sys
import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    names.append(name)
bid_goodbye_to = p.join((names))

print("Adieu, adieu, to "+bid_goodbye_to)
