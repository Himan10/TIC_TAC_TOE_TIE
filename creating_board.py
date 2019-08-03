""" Creating tic-tac-toe board """


def board1():
    """ Printing Board style manually """
    print(
        "              ______ ______ ______ \n \
            |      |      |      |  \n \
            |      |      |      | \n \
            |______|______|______| \n \
            |      |      |      | \n \
            |      |      |      | \n \
            |______|______|______| \n \
            |      |      |      | \n \
            |      |      |      | \n \
            |______|______|______| \n "
    )


def board2():
    """ Printing Board Style Using Iteration """

    board = ""
    for i in range(1, 8):
        if i % 2 != 0:
            board += " ______" * 3
        else:
            board += "|      " * 4
            board += "\n|      |      |      |"
        board += "\n"
    print(board)


def board3():
    """ Printing Board Style Using Iteration Version 2 """
    board = ""
    for i in range(1, 5):
        if i == 1:
            board += " ______" * 3
        else:
            board += "|      " * 4
            board += "\n|      |      |      |"
            board += "\n|______|______|______|"
        board += "\n"
    print(board)


board1()
print()
board2()
print()
board3()
print()
