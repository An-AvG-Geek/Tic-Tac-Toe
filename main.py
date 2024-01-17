positions = {
    1: "0 0",
    2: "0 1",
    3: "0 2",
    4: "1 0",
    5: "1 1",
    6: "1 2",
    7: "2 0",
    8: "2 1",
    9: "2 2",
}


def main():
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    display_board(board)

    check = False
    count = 0
    while check == False:
        board = play(board, count)
        display_board(board)
        check = full(board)

    print("somebody won")

    # while True:
    #     player_1=input("Do you want to choose X or 0 ? ")

    #     if player_1 in ["x","0"]:
    #         break

    #     print("Please Enter a valid input....")


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


def full(board):
    if (
        (board[0][0] and board[0][1]  in ["x", "0"])
        and board[0][0] == board[0][1]
        and board[0][0] == board[0][2]
    ):
        return True
    elif (
        (board[1][0] and board[1][1] in ["x", "0"])
        and board[1][0] == board[1][1]
        and board[1][1] == board[1][2]
    ):
        return True
    elif (
        (board[2][0] and board[2][1]  in ["x", "0"])
        and board[2][0] == board[2][1]
        and board[2][1] == board[2][2]
    ):
        return True

    elif (
        (board[0][0] and board[1][0]  in ["x", "0"])
        and board[0][0] == board[1][0]
        and board[0][0] == board[2][0]
    ):
        return True

    elif (
        (board[0][1] and board[1][1]  in ["x", "0"])
        and board[0][1] == board[1][1]
        and board[0][1] == board[2][1]
    ):
        return True
    elif (
        (board[0][2] and board[1][2]  in ["x", "0"])
        and board[0][2] == board[1][2]
        and board[1][2] == board[2][2]
    ):
        return True
    elif (
        (board[0][0] and board[1][1]  in ["x", "0"])
        and board[0][0] == board[1][1]
        and board[1][1] == board[2][2]
    ):
        return True

    elif (
        (board[2][0] and board[1][1]  in ["x", "0"])
        and board[2][0] == board[1][1]
        and board[1][1] == board[0][2]
    ):
        return True


def play(board, count):
    if count % 2 == 0:
        x = int(input("player 1 where do you want to input "))
        row, col = positions[x].split()

        board[int(row)][int(col)] = "x"
        return board
    else:
        x = int(input("player 1 where do you want to input "))
        row, col = positions[x].split()

        board[int(row)][int(col)] = "0"
        return board


if __name__ == "__main__":
    main()
