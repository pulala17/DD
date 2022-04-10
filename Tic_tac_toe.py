#-----global variables-----

# game board
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-", ]

# if game is still going
game_still_going = True

# who won? or tie?
winner = None

# whose turn is it?
current_player = "X"

# display board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2] ) 
    print(board[3] + "|" + board[4] + "|" + board[5] )        
    print(board[6] + "|" + board[7] + "|" + board[8] )

# play a game of tic tac toe
def play_game():
    
    # Display initial board
    display_board()   

    # while the game is still going
    while game_still_going:

        # handle a single turn of an arbitary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # flip to the other player
        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie. ")    
        

# handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s turn. ")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cannot go there. Go again.")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # set a global variables
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None            
    return


def check_rows():
    # set up global variables
    global game_still_going
    # check if any of rows have all the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row does ahve a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return        


def check_columns():
        # set up global variables
    global game_still_going
    # check if any of rows have all the same value
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    # if any row does ahve a match, flag that there is a win
    if col_1 or col_2 or col_3:
        game_still_going = False
    # return the winner    
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return 


def check_diagonals():
        # set up global variables
    global game_still_going
    # check if any of rows have all the same value
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[2] == board[4] == board[6] != "-"
    # if any row does ahve a match, flag that there is a win
    if dia_1 or dia_2:
        game_still_going = False
    # return the winner    
    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]
    return       


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # global vaariables wwe need
    global current_player
    # if the current player was X , then change to O
    if current_player == "X":
        current_player = "O"
        # if the current plaryer was O, then change to X
    elif current_player == "O":
        current_player = "X"
    return 


play_game()    