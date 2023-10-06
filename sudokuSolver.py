N = 9  # Board size
M = 3  # Sub-grid size

def isValid(board, row, col, num):
    # Check in row, col, and the 3x3 box
    startRow, startCol = M * (row // M), M * (col // M)
    for i in range(N):
        if board[row][i] == num or board[i][col] == num or board[startRow + i // M][startCol + i % M] == num:
            return False
    return True

def solve(board):
    empty = findEmptyCell(board)
    if not empty:
        return True
    row, col = empty

    for i in range(1, N+1):
        if isValid(board, row, col, i):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def findEmptyCell(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return (i, j)
    return None

def printBoard(board):
    for i in range(N):
        if i % M == 0 and i != 0:
            print("-"*21)  # Print horizontal separator
        for j in range(N):
            if j % M == 0 and j != 0:
                print("|", end=" ")  # Print vertical separator
            print(board[i][j], end=" ")
        print()

if __name__ == '__main__':
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solve(board)
    printBoard(board)
