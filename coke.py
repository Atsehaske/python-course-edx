amount_due = 50
while amount_due != 0:
    print("Amount Due: "+str(amount_due))
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin != 25 and inserted_coin != 10 and inserted_coin !=5:
        continue
    else:
        amount_due -= inserted_coin
    if amount_due < 0:
        print("Change Owed: "+str(amount_due*(-1)))
        break
    if amount_due == 0:
         print("Change Owed: "+str(amount_due))
