#GAME ROCK-PAPER-SCISSOR
#------------------------------------------------------------------------
import random
print("Welcome! This program allows you to play the famous game: Rock, paper, scissors! \n")
a = input("Now it's your time to choose, what will you take? Rock, paper or scissors? ")
print ("You chose", a, "!")
a = a.lower()
game_list = ["Rock", "Paper", "Scissors"]
b = random.choice(game_list)
print("The computer chose", b, "!")
b = b.lower()
if a == "rock" and b == "rock":
    print("It's a draw!")
elif a == "rock" and b == "paper":
        print("You lost!")
elif a == "rock" and b == "scissors":
    print("You won!")
elif a == "paper" and b == "rock":
    print("You won!")
elif a == "paper" and b == "paper":
    print("It's a draw!")
elif a == "paper" and b == "scissors":
    print("You lost!")
elif a == "scissors" and b == "rock":
    print("You lost!")
elif a == "scissors" and b == "paper":
    print("You won!")
elif a == "rock" and b == "scissors":
    print("It's a draw!")
else:
    print("Something went wrong.")
    print("Have you typed in your choice correctly?")  
print("Thank you for playing, I hope you had fun!") 
