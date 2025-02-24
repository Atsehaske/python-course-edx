def bank_greeting():
    greeting = input("Greeting: ").lower().strip()
    if greeting[0] == 'h':
        if greeting.endswith("hello",0, 5) == True:
            return "$0"

        return "$20"
    else:
        return "$100"
print(bank_greeting())
