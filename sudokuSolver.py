import random

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
            print("-"*(2*N + M - 1))
        for j in range(N):
            if j % M == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def generateSudoku(difficulty):
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

def getUserInput():
    while True:
        try:
            N = int(input("Enter board size (e.g., 9 for a 9x9 board): "))
            M = int(N**0.5)
            if M * M != N:
                print("Board size must be a perfect square (e.g., 4, 9, 16,...).")
                continue
            
            difficulty = float(input("Enter difficulty (0 to 1, where 1 is hardest): "))
            if not (0 <= difficulty <= 1):
                print("Difficulty must be between 0 and 1.")
                continue

            return N, M, difficulty
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == '__main__':
    N, M, difficulty = getUserInput()
    
    board = generateSudoku(difficulty)

    print("Initial unsolved board:")
    printBoard(board)
    print("\n\n")

    solve(board)
    
    print("Solved board:")
    printBoard(board)
