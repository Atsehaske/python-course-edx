from collections import Counter
def input_list(grocery_list):
    while True:
        try:
            item = input().lower()
        except (EOFError, KeyError):
            break
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

def main():
    grocery_list = {}
    input_list(grocery_list)
    for i in sorted(grocery_list):
      print(grocery_list[i],i.upper())

main()
