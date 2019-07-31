import random

hidden = random.ranrange(1,20)

guess = int(input("enter your number:"))

while True:
    if hidden == guess:
        print("hit!!")
        exit()
    elif hidden > guess:
        print("number is too low")
    else:
        print("number is too high")