import random

def check(answer, expected):
    return answer == expected

def main():
    lvl = get_level()
    i = 0
    score = 0
    wrong_ans_counter = 0
    while i < 10:
        n1, n2 = generate_integer(lvl), generate_integer(lvl)
        while True:
            if wrong_ans_counter == 3:
                print(str(n1)+" + "+str(n2)+" = "+str(n1+n2))
                wrong_ans_counter=0
                break
            try:
                ans = int(input(str(n1)+" + "+str(n2)+" = "))
                if check(ans, n1+n2) is False:
                    wrong_ans_counter+=1
                    raise ValueError
            except ValueError:
                print("EEE")
                continue
            score+=1
            break
        i+=1
    print("Score: "+str(score))
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1,2,3]:
                raise ValueError
            break
        except ValueError:
                continue
    return n

def generate_integer(level):
    if level == 1:
        return random.randrange(0,10)
    elif level == 2:
        return random.randrange(10, 100)
    else:
        return random.randrange(100, 1000)

if __name__ == "__main__":
    main()
