import random
import time as t
name = input("What is your Name?")
t.sleep(0.9)
print("Hello", name ,",Welcome to the Game!!!")
t.sleep(1.2)
word = ['ant','rat','ball','game','item','ship','yellow','parrot','onion']
random_word = random.choice(word)
#print(random_word)
print("Guess from the list", word)
attempt = 6
while(attempt > 0):
    guesstheword = input("Enter your word")
    guess = guesstheword.lower()
    t.sleep(2.5)
    if(random_word == guess):
        print("You Won")
        break
    else:
        attempt -= 1
        if(attempt > 0):
            print("Wrong Guess!", attempt ,"attempt left")
else:
    print("No more attempt left")
    t.sleep(2.5)
    print("Sorry! You lost the game")
