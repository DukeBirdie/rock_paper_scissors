# rock paper scissors
import random as r

def computer():
    num = r.randint(0,2)
    if (num == 0):
        return "rock"
    elif (num == 1):
        return "paper"
    elif (num == 2):
        return "scissors"
    return "Error: Something went wrong."

def player():
    player = input("Rock, Paper, or Scissors: ")
    player.lower()
    if (player == "rock"):
        return "rock"
    if (player == "paper"):
        return "paper"
    if (player == "scissors"):
        return "scissors"

c_points = 0
p_points = 0

while True:
    # while program not terminated
    c = computer()
    p = player()

    if (c == p):
        print("You tied")
        print("Comp Input: ", c)
    elif (c == "rock" and p == "scissors"):
        print("Computer Wins!")
        print("Comp Input: ", c)
        c_points += 1
    elif (c == "paper" and p == "rock"):
        print("Computer Wins!")
        print("Comp Input: ", c)
        c_points += 1
    elif (c == "scissors" and p == "paper"):
        print("Computer Wins!")
        print("Comp Input: ", c)
        c_points += 1
    elif (p == "rock" and c == "scissors"):
        print("Player Wins!")
        print("Comp Input: ", c)
        p_points += 1
    elif (p == "paper" and c == "rock"):
        print("Player Wins!")
        print("Comp Input: ", c)
        p_points += 1
    elif (p == "scissors" and c == "paper"):
        print("Player Wins!")
        print("Comp Input: ", c)
        p_points += 1
    else:
        print("Error: No correct answer")

    print("\n")

    if ((c_points + p_points) == 3): # 3 rounds
        break

if (c_points > p_points):
    print("The computer beat you :(")
else:
    print("You won!! Good job!!")