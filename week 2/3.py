import random
n = random.randint(1, 9)
print(n)
run = bool(True)
i = int(input("Guess a number: "))
while run:
    if i == n:
        print("Congrats!!! You win")
        run = False
    else:
        i = int(input("Guess again: "))