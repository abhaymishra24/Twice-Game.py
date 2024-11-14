
# Here we write code for build Snake-Water-Gun game in Python language-

import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 numbers (variable), you and computer here-

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("Hey!-Its a draw")

else:

    if(computer == -1 and you == 1):
        print("hurry, You win")

    elif(computer == -1 and you == 0):
        print("Oh, You lose")

    elif(computer == 1 and you == -1):
        print("Oh, You lose")

    elif(computer == 1 and you == 0):
        print("hurry, You win")

    elif(computer == 0 and you == -1):
        print("hurry, You win")

    elif(computer == 0 and you == 1):
        print("Oh, You lose")

    else:
        print("Oho, there is some issue")
