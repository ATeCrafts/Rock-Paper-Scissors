import random

computer = random.randint(1, 3)

if computer == 1:
    computer = "R"
elif computer == 2:
    computer = "P"
else:
    computer = "S"

print("Welcome to Rock-Paper-Scissors")

user = input("Enter rock/paper/scissors: ")

options = ["rock", "paper", "scissors"]

while user not in options:
    user = input("Enter rock/paper/scissors: ")

if user == "rock":
    if computer == "R":
        print("Draw")
    elif computer == "P":
        print("You lose :(")
    else:
        print("You win!")
elif user == "paper":
    if computer == "R":
        print("You win!")
    elif computer == "P":
        print("Draw")
    else:
        print("You lose!")
else:
    if computer == "R":
        print("You lose!")
    elif computer == "P":
        print("You win!")
    else:
        print("Draw")