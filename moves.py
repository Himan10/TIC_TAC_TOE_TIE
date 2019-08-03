""" Conditions for making a game TIE """

import random

def random_moves(board, comp_moves, turn):
    """ Making a Move """
    corner = [1, 3, 7, 9]
    #side = [2, 4, 6, 8]

    # Strategies for make a winning move

    if all(board[i] == "     " for i in corner):
        return random.choice(corner)

    if board[5] == "     ":
        return 5

    if board[9] == "     ":  # for 9th move
        if (
                board[1] == turn and board[5] == turn or
                board[3] == turn and board[6] == turn or
                board[7] == turn and board[8] == turn
            ):
            return 9

    if board[8] == "     ":  # for 8th move
        if (
                board[7] == turn and board[9] == turn or
                board[2] == turn and board[5] == turn
            ):
            return 8

    if board[7] == "     ":  # for 7th move
        if (
                board[1] == turn and board[4] == turn or
                board[3] == turn and board[5] == turn or
                board[8] == turn and board[9] == turn
            ):
            return 7

    if board[6] == "     ":  # for 6th move
        if (
                board[3] == turn and board[9] == turn or
                board[4] == turn and board[5] == turn
            ):
            return 6

    if board[5] == "     ":  # for 5th move
        if (
                board[1] == turn and board[9] == turn or
                board[2] == turn and board[8] == turn or
                board[3] == turn and board[7] == turn or
                board[4] == turn and board[6] == turn
            ):
            return 5

    if board[4] == "     ":  # for 4th move
        if (
                board[1] == turn and board[7] == turn or
                board[5] == turn and board[6] == turn
            ):
            return 4

    if board[3] == "     ":  # for 3rd move
        if (
                board[1] == turn and board[2] == turn or
                board[6] == turn and board[9] == turn or
                board[5] == turn and board[7] == turn
            ):
            return 3

    if board[2] == "     ":  # for 2nd move
        if (
                board[5] == turn and board[8] == turn or
                board[1] == turn and board[3] == turn
            ):
            return 2

    if board[1] == "     ":  # for 1st move
        if (
                board[2] == turn and board[3] == turn or
                board[4] == turn and board[7] == turn or
                board[5] == turn and board[9] == turn
            ):
            return 1

    return random.choice(comp_moves)
