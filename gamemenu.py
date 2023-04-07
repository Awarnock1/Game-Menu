from Rockpaperscissors import *
from guessgame import *
from ticTacToe import *

games = {
    1: "Rock paper scissors",
    2: "Number Guess game",
    3: "Tic Tac Toe"
}
Rpsscore = 0
t3score = 0
victory = False
f = open("score.txt", "a")
print("Please enter the title of your save. ")
game_title = input()
while(True):
    print("""
    Your game library:
    1: Rock paper scissors
    2: Number Guess game
    3: Tic Tac Toe
      """)
    choice = input("What game would you like to play,input the corresponding ID number or 'exit' to quit: ")
    if(choice == '1'):
        Rpsscore += play_rockpaperscissors()
        victory = False
        choice = None
    elif(choice == '2'):
        play_guessgame()
        choice = None
    elif(choice == '3'):
        t3score += play_t3()
        choice = None
    elif(choice == "exit"):
        break
f.write(game_title + "\n" + "Rock Paper Scissors Score: " + str(Rpsscore) + "\nTic Tac Toe Score: " + str(t3score) + "\n\n")