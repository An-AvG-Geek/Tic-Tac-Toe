from keys import positions
from pyfiglet import *

name1 = ""
name2 = ""


def main():
    heading()

    global player1
    global player2
    player1, player2 = set_names()

    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    display_board(board)

    check = False
    count = 0
    while check == False:
        board = play(board, count)

        display_board(board)
        count = count + 1

        check = full(board)


def heading():
    print()
    f = Figlet()
    f.setFont(font="slant")
    print(f.renderText("Tic - Tac - Toe"))


def display_board(board):
    print(
        f"""
              -------------
              | {board[0][0]} | {board[0][1]} | {board[0][2]} |
              -------------
              | {board[1][0]} | {board[1][1]} | {board[1][2]} |
              -------------
              | {board[2][0]} | {board[2][1]} | {board[2][2]} |
              -------------
             """
    )


def set_names():
    player1 = input("player 1 : Enter your name ")
    player2 = input("player 2: Enter your name ")
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
