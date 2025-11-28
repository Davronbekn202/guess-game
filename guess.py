import random
def guess_number():
    print("""1-guess number
2-guess word
3-multiplication""")
    pick_one = int(input("choose the option: "))
    if pick_one == 1:
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
    if pick_one == 2:
        while True:
            words = ["Apple,","Banana,","Kiwi,","Mango","Orange","Melon"]
            word = random.choice(words)
            print(*words)
            ask = input("Enter some word (stop): ").title()
            if ask == "stop":
                break
            if ask in word:
                print("you win".upper())
            else:
                print("wrong")
    if pick_one == 3:
        while True:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            ans = num1 * num2
            print(f"{num1} * {num2}")
            first = int(input("enter stop(0): "))
            if first == ans:
                print(f"correct")
            elif first == 0:
                break
            else:
                print(f"wrong, answer-{ans}")


guess_number()
