
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