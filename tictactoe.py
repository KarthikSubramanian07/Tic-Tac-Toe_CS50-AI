"""
Tic Tac Toe Player
"""

import math
import copy

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
    
    if board == initial_state():
        return X
    
    xCount = 0
    oCount = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                xCount += 1
            elif board[i][j] == O:
                oCount += 1
    
    if xCount == oCount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleMoves = set()
    for i in range(0, len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possibleMoves.add((i, j))
    return possibleMoves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
        
    if action not in actions(board):
      raise Exception("Invalid Action")
   
    copyBoard = copy.deepcopy(board)
    copyBoard[action[0]][action[1]] = player(board)
    return copyBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for winner in [X, O]:
        
        #Row check for winner
        for i in range(len(board)):
            if all(board[i][j] == winner for j in range(len(board))):
                return winner

        #Column check for winner
        for j in range(len(board)):
            if all(board[i][j] == winner for i in range(len(board))):
                return winner

        #Diagonal check for winner
        diagonals = [[(0, 2), (1, 1), (2, 0)], [(0, 0), (1, 1), (2, 2)]]
        for diagonal in diagonals:
            if all(board[i][j] == winner for (i, j) in diagonal):
                return winner

    #Tie
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
      return True
    else:
      return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if (winner(board) == X):
            return 1
        elif (winner(board) == O):
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    if current_player == X:
        val = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))
            if k > val:
                val = k
    else:
        val = math.inf
        for action in actions(board):
            k = max_value(result(board, action))
            if k < val:
                val = k
    return action

def max_value(board):
    if terminal(board):
        return utility(board)
    val = -math.inf
    for action in actions(board):
        val = max(val, min_value(result(board, action)))
    return val

def min_value(board):
    if terminal(board):
        return utility(board)
    val = math.inf
    for action in actions(board):
        val = min(val, max_value(result(board, action)))
    return val
