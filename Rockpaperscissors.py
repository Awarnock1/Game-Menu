import random # Needed to generate a computers choice

def rps(one, two, score): # Determines the outcome with the two given choices
    print("Player one has selected: " + one + "\n" + "Player two has selected: " + two) #If player 1 wins score is added to the overall score
    if(one == two):
        print("It's a tie!")
        return score
    elif(one == "r"):
        if(two == "p"):
            print("Player two wins!")
            return score
        if(two == "s"):
            print("Player one wins!")
            score += 1
            return int(score)
    elif(one == "p"):
        if(two == "r"):
            print("Player one wins!")
            score += 1
            return int(score)
        if(two == "s"):
            print("Player two wins!")
            return score
    elif(one == "s"):
        if(two == "r"):
            print("Player two wins!")
            return score
        if(two == "p"):
            print("Player one wins!")
            score += 1
            return score
    elif():
        print("Error!")

def generateComputerChoice(): # Creates computers decision using a random integer between 1 and 3
    choice = random.randint(1, 3)
    if(choice == 1):
        return "r"
    elif(choice == 2):
        return "p"
    elif(choice == 3):
        return "s"
    elif(choice != 1 and choice != 2 and choice != 3):
        print("Error! Random number generation fault.")

def humanGame(score):
    while(True):
        print("Player 1 please enter (r)ock (p)aper or (s)cissors")
        player1 = str(input())
        if(player1 != "r" and player1 != "p" and player1 != "s"):
            print("Please enter 'r', 'p', or 's'")
            continue
        else:
            break
    while(True):
        print("Player 2 please enter (r)ock (p)aper or (s)cissors")
        player2 = str(input())
        if(player2 != "r" and player2 != "p" and player2 != "s"):
            print("Please enter 'r', 'p', or 's'")
            continue
        else:
            break
    score = rps(player1, player2, score)
    return int(score)

def compGame(score):
    while(True):
        print("Player 1 please enter (r)ock (p)aper or (s)cissors")
        player = str(input())
        if(player != "r" and player != "p" and player != "s"):
            print("Please enter 'r', 'p', or 's'")
            continue
        else:
            break
    computer = generateComputerChoice()
    score = rps(player, computer, score)
    return score

def play_rockpaperscissors(): # Prompts player to decide if they want to play against a player or computer
    print("Welcome to Rock Paper Scissors!")
    success = False
    score = 0
    while(success == False): # While function to loop through if they do not input p or c
        print("Would you like to play against the (c)omputer or another (p)layer?")
        compOrPlayer = input()
        compOrPlayer = compOrPlayer.lower()
        if(compOrPlayer == "p" or compOrPlayer == "player"):   
            score = humanGame(int(score))
            print(score)
            success = True
        elif(compOrPlayer == "c" or compOrPlayer == "computer"):
            score = compGame(score)
            print(score)
            success = True
        if(success == True):
            boole = False
            while(True):
                print("Would you like to play again? (y)es or (n)o")
                again = input()
                again = again.lower()
                if(again == "y"):
                    success = False
                    break
                elif(again == "n"):
                    success = True
                    break
                else:
                    print("Please enter 'y' or 'n'")
        elif(compOrPlayer != "c" and compOrPlayer != "p"):
            print("Error! Please enter 'p' or 'c'")
    return score