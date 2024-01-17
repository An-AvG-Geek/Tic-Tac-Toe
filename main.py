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

name1 = ""
name2 = ""


def main():
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


def full(board):
    if (
        (board[0][0] and board[0][1] in ["x", "0"])
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
        (board[2][0] and board[2][1] in ["x", "0"])
        and board[2][0] == board[2][1]
        and board[2][1] == board[2][2]
    ):
        return True

    elif (
        (board[0][0] and board[1][0] in ["x", "0"])
        and board[0][0] == board[1][0]
        and board[0][0] == board[2][0]
    ):
        return True

    elif (
        (board[0][1] and board[1][1] in ["x", "0"])
        and board[0][1] == board[1][1]
        and board[0][1] == board[2][1]
    ):
        return True
    elif (
        (board[0][2] and board[1][2] in ["x", "0"])
        and board[0][2] == board[1][2]
        and board[1][2] == board[2][2]
    ):
        return True
    elif (
        (board[0][0] and board[1][1] in ["x", "0"])
        and board[0][0] == board[1][1]
        and board[1][1] == board[2][2]
    ):
        return True

    elif (
        (board[2][0] and board[1][1] in ["x", "0"])
        and board[2][0] == board[1][1]
        and board[1][1] == board[0][2]
    ):
        return True
    else:
        return False


def play(board, count):
    if count%2==0:
        value=int(input(f"{player1} where do you want to input "))
        row,col=positions[value].split()
        board[int(row)][int(col)]='x'
        

    else:
        value=int(input(f"{player2} where do you want to input "))
        row,col=positions[value].split()
        board[int(row)][int(col)]='0'

    return board


    
    
    


if __name__ == "__main__":
    main()



    