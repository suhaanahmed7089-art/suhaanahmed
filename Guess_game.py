# Creating a guess game

import random
print("----Welcome to guess game----")
print("I am guessing a no. between 1 to 10")
number=random.randint(1,10)
attempts=0
while True:
    try:
        # taking user input
        guess=int(input("Guess a no: "))
        attempts=attempts+1
        if(guess==number):
            print(f"Comgratulations! you guessed the correct answer in {attempts} attempts")
        else:
            print("Wrong answer, try guessing again")
    except ValueError:
        print("please enter an integer")

