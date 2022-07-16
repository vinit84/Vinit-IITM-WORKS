#Number Guessing Game

import random

num = random.randint(1,100)
winning_number=num
user=int(input("Guess  the number \U0001F914 ? "))

if (user==winning_number):
    print("\U0001F973 You won !!")
elif(user<winning_number):
    print("\U0001F612 You are too low !")
else:
    print(" \U0001F62C too high")


