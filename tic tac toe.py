#Zach P
#12/10
#Tic-Tac-Toe
name = input("Enter your name: ")
x = "X"
o = "O"
empty = " "
tie = "Tie"
num_squares = 9
def display_instructions():
    """Display game instructions."""
    print(
    """
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

def ask_permission(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question+"y or n").lower()
    return response

def ask_num(question,low, high):
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
                break
            elif response not in range(low, high):
                response = input(question)
        else:
            print("Invalid, try again")
            response = input(question)
    return int(response)




x =ask_num("Input a number between 0 and 8 ",0, 9)
print(x)
            
























































    
