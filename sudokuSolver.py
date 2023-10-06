import random

N = 9  #Board size
M = 3  #Sub-grid size

def isValid(board, row, col, num):
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

    nums = list(range(1, N+1))
    random.shuffle(nums)

    for i in nums:
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

def generateSudoku(difficulty=0.5):
    board = [[0]*N for _ in range(N)]
    solve(board)

    totalCells = N * N
    numToRemove = int(difficulty * totalCells)

    while numToRemove > 0:
        row = random.randint(0, N-1)
        col = random.randint(0, N-1)
        if board[row][col] != 0:
            board[row][col] = 0
            numToRemove -= 1

    return board

if __name__ == '__main__':
    board = generateSudoku()

    print("Initial unsolved board:")
    printBoard(board)
    print("\n\n")

    solve(board)
    
    print("Solved board:")
    printBoard(board)
