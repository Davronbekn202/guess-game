import random


def guess_number():
    while True:
        numbers = random.randint(1, 100)
        choose = int(input("pick number from 1 to 100 stop(0): "))
        if choose == numbers:
            print(f"You win it was {choose}")
        elif choose == 0:
            break
        elif choose != numbers:
            print("You are wrong")
        else:
            print("Enter valid number")


guess_number()
