
# Here we write code for build Guess-Perfect-Number game in Python language-

import random

n = random.randint(1, 100)
a = -1
guesnum = 1

while (a != n):

    a = int(input("Guess the number: "))

    if (a>n):
        print("select lower number")
        guesnum += 1

    elif (a<n):
        print("select higher number")
        guesnum += 1

print(f"Hurry 🤩, You guess it the number {n} correct in {guesnum} attempts.")
print("Congratulation🥳", "Let's play once again!")
