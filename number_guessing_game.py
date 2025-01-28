import random
import art
print(art.logo)
#define a function to get random number from 0 to 100
def random_number():
    return random.randint(1,100) 
#defining a compare function 
def compare(x,y):
    if x==y:
        return "you win"
    elif x>y:
        return "too high"
    else:
        return "too low"
r_number=random_number() 
#if mode if hard or easy
mode=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if mode=="hard":
    attempts=5
else:
    attempts=10
print("I'm thinking of a number between 1 and 100.")
#if attempt does not equal to zero this loop runs
while attempts!=0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    #user guess
    user_guess=int(input("Make a guess:"))
    #store the compared value by calling the compare function
    compared=compare(user_guess,r_number)
    #compare equal win then attempt==0
    if compared=="you win":
        print(f"You got it! The answer was {r_number}.")
        attempts=0
    #if no then attempt is redused by 1 and guess agin print
    else:
        attempts-=1
        print(compared)
        print("Guess again")
        #if attempts==0 by reducing then run out of guesses
        if attempts==0:
            print("You've run out of guesses. you lose")






