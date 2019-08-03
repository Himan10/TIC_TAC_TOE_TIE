# Customizing board
""" Playing Tic Tac Toe with Computer """

import random
import moves


BOARD_VALUE = {}
for number in range(1, 10):
    BOARD_VALUE[number] = "     "

COMP_MOVES = BOARD_VALUE.keys()
COMP_MOVES = list(COMP_MOVES)


def computer_play(turn):
    """ Computer move on the board """
    comp_val = moves.random_moves(BOARD_VALUE, COMP_MOVES)
    print(" Computer Move : ", comp_val)
    BOARD_VALUE[comp_val] = turn
    del COMP_MOVES[COMP_MOVES.index(comp_val)]


def user_play(turn):
    """ User move on the board """
    user_val = int(input(" Make your Move : "))
    BOARD_VALUE[user_val] = turn
    del COMP_MOVES[COMP_MOVES.index(user_val)]


def print_board():
    """ Printing the Board """
    print(" _____ _____ _____")
    print("|     |     |     |")
    print(f"|{BOARD_VALUE[1]}|{BOARD_VALUE[2]}|{BOARD_VALUE[3]}|")
    print("|     |     |     |")
    print(" -----+-----+-----")
    print("|     |     |     |")
    print(f"|{BOARD_VALUE[4]}|{BOARD_VALUE[5]}|{BOARD_VALUE[6]}|")
    print("|     |     |     |")
    print(" -----+-----+-----")
    print("|     |     |     |")
    print(f"|{BOARD_VALUE[7]}|{BOARD_VALUE[8]}|{BOARD_VALUE[9]}|")
    print("|_____|_____|_____|")


def winner(turn):
    """ Win the Game """
    return ((BOARD_VALUE[1] == turn and BOARD_VALUE[2] == turn and BOARD_VALUE[3] == turn) or
            (BOARD_VALUE[4] == turn and BOARD_VALUE[5] == turn and BOARD_VALUE[6] == turn) or
            (BOARD_VALUE[7] == turn and BOARD_VALUE[8] == turn and BOARD_VALUE[9] == turn) or
            (BOARD_VALUE[1] == turn and BOARD_VALUE[4] == turn and BOARD_VALUE[7] == turn) or
            (BOARD_VALUE[2] == turn and BOARD_VALUE[5] == turn and BOARD_VALUE[8] == turn) or
            (BOARD_VALUE[3] == turn and BOARD_VALUE[6] == turn and BOARD_VALUE[9] == turn) or
            (BOARD_VALUE[1] == turn and BOARD_VALUE[5] == turn and BOARD_VALUE[9] == turn) or
            (BOARD_VALUE[3] == turn and BOARD_VALUE[5] == turn and BOARD_VALUE[7] == turn))


def main():
    """ Main function """
    comp_turn = "  o  "
    chance = random.randint(0, 1)  # 0 for user and 1 for computer
    try:
        user_turn = "  " + str(input(" 'x' or 'o' : ")) + "  "
        if user_turn == "  o  ":
            comp_turn = "  x  "

        for i in range(chance, chance + 9):  # chance == 0 then we've 0-9
            # and chance == 1 then we've 1-10
            if i % 2 != 0:
                user_play(user_turn)
                win = winner(user_turn)
            else:
                computer_play(comp_turn)
                win = winner(comp_turn)
            print_board()
            if win:
                print(" WINNNEEEERRRRR ")
                break

    except (IndexError, ValueError) as err:
        print(err)


main()
