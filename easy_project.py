# # MINI PROJECT_01
"""GUESS THE NUMBER GAME"""

import random as rd


target = rd.randint(1,100)

try:
    while True:
        userNum = input("Guess the number or Quit(press Q) : ")
        if userNum == "Q" or userNum == "q":
            break
        userNum = int(userNum)
        if userNum == target:
            print(f"You've guessed successfully.")
            break
        elif userNum > target:
            print(f"Nice try! Guess lower!")
        elif userNum < target:
            print(f"Nice try! Guess higher!")
    print(f"_____GAME OVER_____")

except Exception as e:
    print(f"INVALID INPUT!! PLEASE INPUT A VALID INTEGER")