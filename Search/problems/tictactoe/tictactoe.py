"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # if board == initial_state():
    #     return X
    
    xs = 0
    os = 0

    for l in board:
        for v in l:
            if v == X:
                xs += 1
            if v == O:
                os += 1
    
    if xs > os:
        return O
    else:
        return X    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible = set()

    for l in board:
        for v in l:
            if v == EMPTY:
                possible.add((l,v))
    
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
