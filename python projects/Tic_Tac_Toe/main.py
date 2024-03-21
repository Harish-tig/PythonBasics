# from IPython.display import clear_output
# from Ipython.display import clear_output0
# import random

#intermediate code
# Board is of list and update based on index. get index via user in put
# start game by assign X and O to player via input if user 1 chose x automatically o to user 2 and return a tuple
# create a function for win check
# create a play function and check win 4 each time a player makes a move
# create a replay function to call main
# define main function to assemble game logic
#keep the above algo same and reverse the tuple

from colorama import Fore
from colorama import init
init()
def display_board(board):
    print(Fore.RED, (board[7] + "|" + board[8] + "|" + board[9]))
    print("- - - - ")
    print(Fore.RED, (board[4] + "|" + board[5] + "|" + board[6]))
    print("- - - - ")
    print(Fore.RED, (board[1] + "|" + board[2] + "|" + board[3]))
    return board

def start():
    player1 = input("Player 1 ----> Choose X or O: ")
    while player1 not in ["X", "x", "o", "O"]:
        print("invalid input choose X or O")
        player1 = input("Player 1 ----> Choose X or O: ")

    if player1 in ("X", "x"):
        player2 = "O"
    else:
        player2 = "X"

    print("player 1 is {a} and player 2 is {b}".format(a=player1, b=player2))
    return (player1,player2)


def win_check(board, tuple):  # board to check line if won or not # returns boolean
    if ((board[1] == board[2] == board[3] == tuple[0]) or
            (board[4] == board[5] == board[6] == tuple[0]) or
            (board[7] == board[8] == board[9] == tuple[0]) or
            (board[1] == board[4] == board[7] == tuple[0]) or
            (board[5] == board[2] == board[8] == tuple[0]) or
            (board[3] == board[6] == board[9] == tuple[0]) or
            (board[1] == board[5] == board[9] == tuple[0]) or
            (board[3] == board[5] == board[7] == tuple[0])):
        return True
    else:
            return False


x = None


def play(player, board):  # tuple (X, O) index 0,1
    if win_check(board, player):
        player1 = int(input("player 1 choose a position: "))
        while player1 not in range(1, 10):
            print("Enter a valid position in range 1 to 9")
            player1 = int(input("player1 choose a position: "))
        board[player1] = player
        display_board(board)
    return board


def replay():
    check = input("Do you want to play again?: (Y or N) ")
    while check not in ["Y", "N"]:
        check = input("Invalid input, Do you want to play again?: (Y or N) ")
    if check == "Y":
        main()
    else:
        exit(0)


def main():
    # Initialize
    game_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    display_board(game_board)
    players = start()
    player = players[0]

    while True:
        play(board=game_board, player = player)
        # Check for a winner
        if win_check(game_board, players):
            print(f"Player {x} wins!")
            break
        # Check for a tie
        if " " not in game_board:
            print("It's a tie!")
            break

    replay()
    players = reversed(players)

main()