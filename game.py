import random

n = -1
while n<1 or n>99:
    try:
        n = int(input("level: "))
    except ValueError:
        pass
random_number = random.randrange(1, n+1)

while True:
    try:
        guessed = int(input("Guess: "))
        if random_number<guessed:
            print("Too large!")
        elif random_number>guessed:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass

