"""
Tic Tac Toe Player
"""
import copy
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
    xCount = 0
    OCount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                xCount += 1
            elif board[i][j] == 'O':
                OCount += 1

    return 'X' if xCount == OCount else 'O'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    emptySpace = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                emptySpace.add((i, j))
    return emptySpace

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    curPlayer = player(board)
    i, j = action
    newBoard = copy.deepcopy(board)
    newBoard[i][j] = curPlayer
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return bool(winner(board)) or not(actions(board))

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        winPlayer = winner(board)
        if winPlayer == 'X':
            return 1
        elif winPlayer == 'O':
            return -1
        else:
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board[1][1] == EMPTY:
        return 0, (1, 1)

    if terminal(board):
        return utility(board), None

    curPlayer = player(board)
    candidates = actions(board)
    resultMove = []
    for a, b in candidates:
        board[a][b] = curPlayer
        state = minimax(board)
        value, _ = state
        board[a][b] = EMPTY
        if not resultMove and value == 0:
            resultMove = (a, b)
        if curPlayer == 'X':
            if value == 1:
                return value, (a, b)
        if curPlayer == 'O':
            if value == -1:
                return value, (a, b)

    if not resultMove:
        return value, (a, b)
    else:
        return 0, resultMove
