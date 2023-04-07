BOARD = {1: ' ',  2: ' ',  3: ' ',

        4: ' ',  5: ' ',  6: ' ',

        7: ' ',  8: ' ',  9: ' '}


def render():
    '''
    Returns a string describing the board in its
    current state. It should look something like this:

     1 | 2 | 3
     - + - + -
     4 | 5 | 6
     - + - + -
     7 | 8 | 9

    Returns
    -------
    board_state : str

    Implements (See also)
    ---------------------
    BOARD : dict
    '''
    return str(BOARD[1] + " | " + BOARD[2] + " | " + BOARD[3] + "\n" + BOARD[4] + " | " + BOARD[5] + " | " + BOARD[6] + "\n" + BOARD[7] + " | " + BOARD[8] + " | " + BOARD[9])

def get_action(player):
    '''
    Prompts the current player for a number between 1 and 9.
    Checks* the returning input to ensure that it is an integer
    between 1 and 9 AND that the chosen board space is empty.

    Parameters
    ----------
    player : str

    Returns
    -------
    action : int

    Raises
    ======
    ValueError, TypeError

    Implements (See also)
    ---------------------
    BOARD : dict

    *Note: Implementing a while loop in this function is recommended,
    but make sure you aren't coding any infinite loops.
    '''
    print(player + " please select a board space.")
    while(True):
        move = int(input())
        if(int(move) < 1 or int(move) > 10):
            print(player + " please select a free space between 1 and 9.")
        elif(BOARD[int(move)] != " "):
            print("That space is taken already please select another one.")
        elif(BOARD[int(move)] == " "):
            BOARD[int(move)] = player
            print(render())
            return 0
    


def victory_message(player):
    '''
    Prints the updated board and returns a victory message for the
    winning player.

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    victory_message : str

    Implements (See also)
    ---------------------
    print_t3() : func
    '''
    print(render())
    return "Congratulations " + player + " you have won the game!"


def check_win(player):
    '''
    Checks victory conditions. If found, calls victory_message().
    This can be done with one long chain of if/elif statements, but
    it can also be condensed into a single if/else statement, among
    other strategies (pattern matching if you have python 3.10 or above).

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    BOARD : dict
    victory_message(player) : func
    '''
    if(BOARD[1] == player and BOARD[2] == player and BOARD[3] == player):
        print(victory_message(player))
        return True
    elif(BOARD[1] == player and BOARD[4] == player and BOARD[7] == player):
        print(victory_message(player))
        return True
    elif(BOARD [3] == player and BOARD[6] == player and BOARD[9] == player):
        print(victory_message(player))
        return True
    elif(BOARD[7] == player and BOARD[8] == player and BOARD[9] == player):
        print(victory_message(player))
        return True
    elif(BOARD[4] == player and BOARD[5] == player and BOARD[6] == player):
        print(victory_message(player))
        return True
    elif(BOARD[7] == player and BOARD[8] == player and BOARD[9] == player):
        print(victory_message(player))
        return True
    elif(BOARD[2] == player and BOARD[5] == player and BOARD[8] == player):
        print(victory_message(player))
        return True
    elif(BOARD[1] == player and BOARD[5] == player and BOARD[9] == player):
        print(victory_message(player))
        return True
    elif(BOARD [3] == player and BOARD[5] == player and BOARD[7] == player):
        print(victory_message(player))
        return True
    else:
        return False

def initializeBOARD():
    for i in range(1,10):
        BOARD[i] = " "

def play_t3():
    '''
    This is the main game loop that is called from the launcher (main.py)

    Implements (See also)
    ---------------------
    BOARD : dict
    render() : func
    get_action(player) : func
    check_win(player) : func
    play_t3()* : func

    *Note: this function refers to itself. Be careful about
    inescapable infinite loops.
    '''
    score = 0
    player = 'X'
    player2 = 'Y'
    again = True
    print("Welcome to Tic Tac Toe!")
    while(again == True):
        game_over = False #Reinitializes values each game if player chooses to play again
        game_round = 0
        initializeBOARD()
        print(render()) #Prints the starting board post initialization
        while not game_over:        
            get_action(player) #gets players action
            game_over = check_win(player) #checks if player has met winning criteria
            if(game_over == True):
                score += 1 #increments score
                break #ends game
            if(game_round >= 4): #After Player 1's 5th turn there are no more spaces 
                print("It's a tie!")
                game_over = True
                break
            get_action(player2)
            game_over = check_win(player2)
            if(game_over == True):
                break
            game_round += 1
        while(True):
            print("Would you like to play again? (y)es or (n)o")
            ans = input()
            if(ans == "y"):
                again = True
                break
            elif(ans == "n"):
                again = False
                break
            else:
                print("Please enter y or n")
    return score
        

        # Delete this line when you're ready to run the loop.

        # Print the current state of the board

        # Get the current player's action and assign it to a variable called 'action'.

        # Assign the current player ('X' or 'O') as a value to BOARD. Use the 'action' variable as the key.

        # Increment the game round by 1.

        # Check if the game is winnable (game_round >= 4),
            # then check for win conditions (check_win(player)),
                # and if there's a win, end the game (game_over = True),
                # and break the loop (break).

        # Check if there are any open spots left (game_round == 9),
            # and if there aren't, print a tie message,
            # end the game,
            # and break the loop.

        # switch players with a quick conditional loop.


    # prompt for a restart and assign the input to a 'restart' variable.
    # if yes,
        # clear each key in the board with a for loop
            
        # and reinitiate the game loop (play_t3()).
