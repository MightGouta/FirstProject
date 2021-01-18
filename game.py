#ask name of user
name = input("Hi, I'm Swit, python's bot. What's your name? " )
print()

#greets the user
print("hello,", name,", nice to meet you!")
print("I want to become your friend", name)
print()

#ask the age of the user
age = input("How old are you? ")
print("Oh nice, you are", age, "years old! You're old enough to play my game!")
print()

#ask if the user wants to play the game
answer = input("Do you want to play? yes or no? " )

if answer == "no":
    print("That's unfortunate, I had a nice guessing game. ")

else:
    print("yayyy I have a nice guessing game for you! ")
print()

game = input("are you ready?? ")
print()

if game == "no":
    print("I said are your READY??")

else:
    print("ok then, let's startttt")

print("here are the rules of the game, I have a number from 1 to 10 in my head, and you have 3 tries to guess it. If you get it right, you win otherwise I do :) ")
print()
print("Go!")

#play the game
import random

def main():
    number = random.randint(1, 10)

    for i in range(3):
        guess = int(input("Guess: "))
        if guess > number:
            print("Guess is too large")
        elif guess < number:
            print("Guess is too small")
        else:
            print("Correct!")
            return

main()
print()

#ask the user if he won
win = input("so did you win or no? " )
print

if win == "no":
    print("That's unfortunate, you can try again")

else:
    print("Awesome! I knew I should've increased the range of difficulty! ")

#ask the user if he wants to play again
answer = input("Do you want to play with increase difficulty? yes or no? " )

if answer == "no":
    print("That's unfortunate, I wanted to take revenge. ")

else:
    print("perfect, this time you won't win ")
    print("This time you have 4 tries, but the range goes from 1 to 20")
print()

game = input("are you ready?? ")
print()

if game == "no":
    print("I said are your READY??")

else:
    print("ok then, let's startttt")


#the game with increased difficulty, Lvl2
import random

def main():
    number = random.randint(1, 20)

    for i in range(4):
        guess = int(input("Guess: "))
        if guess > number:
            print("Guess is too large")
        elif guess < number:
            print("Guess is too small")
        else:
            print("Correct!")
            return

main()
print()

#ask the user if he won
win = input("so did you win this time with increased difficulty or no? " )
print

if win == "no":
    print("YES, I finally beat you!!!")

else:
    print("Ah man, you won again. I thought I had a chance. ")
print()

final = input("There is a final level, do you want to try? " )
print()

if final == "no":
    print("Ok, have a good day." )

else:
    print("Ok let's do it")

final = input("For this level, you have 7 guesses to try and figure out a number between 1 and 100 are you ready? ")

if final == "no":
    print("ok, have a nice one!")

else:
    print("let's go, the final round :)")

#The final level
import random

def main():
    number = random.randint(1, 100)

    for i in range(7):
        guess = int(input("Guess: "))
        if guess > number:
            print("Guess is too large")
        elif guess < number:
            print("Guess is too small")
        else:
            print("Correct!")
            return
main()

#Ask the user one last question
last = input("did you win the last round? ")
print()
if last == "no":
    print("I knew it, there's no way you could've won! :))")
    print("anyways, have a good one", name,"!")

else:
    print("WHAT??!!?! You know what? I give up!")
    print("have a good one", name,"!")
    print("It was a pleasure to meet you!")
print()
print("If you type CTRL + L, you can erase the terminal and type 'python game.py' to restart :)")
print()
print("Ok, now bye", name,"!")

#end
#this is my first personnal code after a CS50 seminar showing us how to do loops, conditions, arithmetics, etc
#please comment if you know how one could optimize this text in order for it to be shorter and more efficient.
