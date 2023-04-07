import random # Needed to make the random number to guess

def interact(max):
    goal = random.randint(0, max)
    print("Please take your first guess, your number is somewhere between 1 and " + str(max) + "!")
    counter = 0 #Tracks how many guesses the user took
    while(True):
        guess = input()
        guess = int(guess)
        if(guess > goal and guess <= max): #Guessed over the value
            print("Your guess " + str(guess) + " is too high!")
            counter += 1
        elif(guess < goal and guess >= 1): #Guessed under the value
            print("Your guess " + str(guess) + " is too low!")
            counter += 1
        elif(guess == goal): #User guessed correctly
            counter += 1
            print("You got it! Congrats you got it in " + str(counter) + " guesses!") #Prints how many guesses it took
            break
        elif(guess > max or guess < 1): #Incase user guesses too high or low and does not count as a guess
            print("Answer cannot be " + str(guess) + ". Please guess within the range of 1 and " + str(max) + ".")


def play_guessgame():
    print("""
    Welcome to the Number Guess Game!
    Please select your difficulty
    1: Very easy (1-10)
    2: Easy (1-25)
    3: Medium(1-50)
    4: Hard (1-100)
    5: Very hard (1-500)
    """)
    while(True):
        difficulty = int(input()) # Changes max number the random variable can be
        if(difficulty == 1):
            gmax = 10
            break
        elif(difficulty == 2):
            gmax = 25
            break
        elif(difficulty == 3):
            gmax = 50
            break
        elif(difficulty == 4):
            gmax = 100
            break
        elif(difficulty == 5):
            gmax = 500
            break
        else:
            print("Please select a difficulty from 1-5") #incase user puts in anything not 1, 2, 3, 4, or 5
    interact(gmax)
