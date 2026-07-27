import art
import random as r

#TODO-1 display the logo and "Welcome to the Number Guessing Game!"
print(art.logo)
print("Welcome to the Number Guessing Game!")

#TODO-2 choose a random number between 1-100 and assign it to at a variable
# and display "I'm thinking of a number between 1 and 100."
number=r.randint(1,100)
print("I'm thinking of a number between 1 and 100.")


#TODO-3 create a variable named as "attempts" and display
# "Choose a difficulty. Type 'easy' or 'hard': "
attempts=0
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")

#TODO-4 update the attempts variable according to user's choice(easy:10,hard:5)
if difficulty=="easy":
    attempts=10
elif difficulty=="hard":
    attempts=5

#TODO-5 inside a loop check user's guess and display remaining attempts
# if guess is not correct display: Too low./Too high
# "You have x attempts remaining to guess the number."
# and display "Make a guess: "
game_ended = False
while not game_ended:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess == number:
        game_ended = True
        print(f"You got it! The answer was {number}.")
    elif guess != number and attempts!=0:
        attempts-=1
        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            break
        elif guess<number:
            print("Too low")
        elif guess>number:
            print("Too high")
        print("guess again")




#TODO-6 and after the guesses if user wins display "You got it! The answer was 87."
# if user loose display "You've run out of guesses. Refresh the page to run again."
# and program ens






















