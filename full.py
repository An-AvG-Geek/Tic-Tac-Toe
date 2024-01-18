def full(board):
    not_draw = 0

    for i in board:
        for j in i:
            if j not in ["x", "0"]:
                not_draw = 1

    if not_draw == 0:
        return True, 0

    if (
        (board[0][0] and board[0][1] in ["x", "0"])
        and board[0][0] == board[0][1]
        and board[0][0] == board[0][2]
    ):
        if board[0][0] == "x":
            return True, 1

        else:
            return True, 2

    elif (
        (board[1][0] and board[1][1] in ["x", "0"])
        and board[1][0] == board[1][1]
        and board[1][1] == board[1][2]
    ):
        if board[1][0] == "x":
            return True, 1
        else:
            return True, 2

    elif (
        (board[2][0] and board[2][1] in ["x", "0"])
        and board[2][0] == board[2][1]
        and board[2][1] == board[2][2]
    ):
        if board[2][0] == "x":
            return True, 1
        else:
            return True, 2

    elif (
        (board[0][0] and board[1][0] in ["x", "0"])
        and board[0][0] == board[1][0]
        and board[0][0] == board[2][0]
    ):
        if board[0][0] == "x":
            return True, 1
        else:
            return True, 2

    elif (
        (board[0][1] and board[1][1] in ["x", "0"])
        and board[0][1] == board[1][1]
        and board[0][1] == board[2][1]
    ):
        if board[0][1] == "x":
            return True, 1
        else:
            return True, 2

    elif (
        (board[0][2] and board[1][2] in ["x", "0"])
        and board[0][2] == board[1][2]
        and board[1][2] == board[2][2]
    ):
        if board[0][2] == "x":
            return True, 1
        else:
            return True, 2

    elif (
        (board[0][0] and board[1][1] in ["x", "0"])
        and board[0][0] == board[1][1]
        and board[1][1] == board[2][2]
    ):
        if board[0][0] == "x":
            return True, 1
        else:
            return True, 2

    elif (
        (board[2][0] and board[1][1] in ["x", "0"])
        and board[2][0] == board[1][1]
        and board[1][1] == board[0][2]
    ):
        if board[2][0] == "x":
            return True, 1
        else:
            return True, 2

    else:
        return False, 3
