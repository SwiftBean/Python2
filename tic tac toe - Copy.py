#Zach P
#12/10
#Tic-Tac-Toe
name = input("Enter your name: ")
x = "X"
o = "O"
empty = " "
tie = "Tie"
num_squares = 9
#####################################################################
def display_instructions():
    """Display game instructions."""
    print(
    name, """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move known by entering a number, 0 - 8. The number
    will correspond to the board position as illustrated:

                0 | 1 | 2
                -----------
                3 | 4 | 5
                -----------
                6 | 7 | 8

    Prepare yourself human......
    """
    )
#####################################################################
def ask_permission(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question+"y or n").lower()
    return response
#####################################################################
def ask_num(question,low, high):
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                response = input(question)
        else:
            print("Invalid, try again")
            response = input(question)
    return int(response)
#####################################################################
def pieces():
    go_first = ask_permission("Do you want to go first? y or n?: ")
    if go_first == "y":
        print("\nYeah I think you need the headstart.")
        human = x
        computer = o
    else: 
        print("\nOh, you think you're better than a computer?")
        computer = x
        human = o
    return computer, human
#####################################################################
def new_board():
    """Create a new game board."""
    board = []
    for square in range(num_squares):
        board.append(empty)
    return(board)
#####################################################################
def display_board(board):
    """Display board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")
#####################################################################
def legal_moves(board):
    """Create a list of legal moves"""
    moves = []
    for square in range(num_squares):
        if board[square] == empty:
            moves.append(square)
    return moves 
#####################################################################
def winner(board):
    """Determine the game winner."""
    ways_to_win = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner

    if empty not in board:
        return tie
    
    return None
#####################################################################
def human_move(board):
    """Get human move."""
    op = legal_moves(board)
    move = None
    while move not in op:
        move = ask_num("Where will you move? (0 - 8): ", 0, num_squares)
        if move not in op:
            print("\nThat's not a legal move you fool")
        else:
            print("Fine..")
            return move
#####################################################################       
def next_move(turn):
    """Switch turns."""
    if turn == x:
        return o
    else:
        return x
#####################################################################
def congrat_winner(the_winner, computer, human):
    """Congragulate the winner."""
    if the_winner != tie:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")
    if the_winner == computer:
        print("Ha, you got beat by a computer, you suck")
    elif the_winner == human:
        print("So you've beaten me... I hope you enjoyed it.")
    elif the_winner == tie:
        print("It seems that we have a tie... try harder next time.")
#####################################################################    
def computer_move(board, computer, human):
    """Make computer move."""
    # Make a copy to work with since function will be changing list
    board = board[:]
    # The best posiotions to have in order
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take square number", end=" ")

    #if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
    #done checking this move, undo it
        board[move] = empty

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = empty

    #since no one can win on next move, pick best open square
    for move in best_moves:
        if move in legal_moves(board):
            print(move)
            return(move)
#####################################################################
def main():
    display_instructions()
    computer, human = pieces()
    turn = x
    board = new_board()
    new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_move(turn)
    win = winner(board)
    congrat_winner(win, computer, human)

main()
            


            
























































    
