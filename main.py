from keys import positions
from pyfiglet import *
from full import full
from display import display_board

name1 = ""
name2 = ""


def main():
    while True:

        heading()

        global player1
        global player2
        player1, player2 = set_names()

        board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        display_board(board)

        check = False
        count = 0
        while check == False:
            try:
                board = play(board, count)

                display_board(board)
                count = count + 1

                check,player = full(board)
            except (ValueError,KeyError):
                print("Enter valid value (1-9) ")

                print()
                continue

        if player==1:
            print(f"{player1} has won ")
        elif player==2:
            print(f"{player2} has won ")
        elif player==0:
            print("the game has ended in a draw")

        cont=input("do you want to continue (y/n) ").lower().strip()
        if count=='n':
            print("exiting from program....")
            break




def heading():
    print()
    f = Figlet()
    f.setFont(font="slant")
    print(f.renderText("Tic - Tac - Toe"))





def set_names():
    player1 = input("player 1 : Enter your name ").strip().capitalize()
    player2 = input("player 2: Enter your name ").strip().capitalize()
    return player1, player2




def play(board, count):
    while True:
        if count % 2 == 0:
            value = int(input(f"{player1} where do you want to input "))

        else:
            value = int(input(f"{player2} where do you want to input "))

        if validate(value, board) == True:
            row, col = positions[value].split()
            if count % 2 == 0:
                board[int(row)][int(col)] = "x"

            else:
                board[int(row)][int(col)] = "0"

            break

    return board


def validate(value, board):
    row, col = positions[value].split()
    if board[int(row)][int(col)] not in ["x", "0"]:
        return True


if __name__ == "__main__":
    main()
