import random
import time

def isValid(num, row, col):
    boxIndex = (row // M) * M + col // M

    if num in rows[row] or num in cols[col] or num in boxes[boxIndex]:
        return False
    
    return True

def placeNumber(board, num, row, col):
    boxIndex = (row // M) * M + col // M
    board[row][col] = num
    rows[row].add(num)
    cols[col].add(num)
    boxes[boxIndex].add(num)

def removeNumber(board, row, col):
    boxIndex = (row // M) * M + col // M
    removed = board[row][col]
    board[row][col] = 0
    rows[row].remove(removed)
    cols[col].remove(removed)
    boxes[boxIndex].remove(removed)

def solve(board):
    empty = findEmptyCell(board)

    if not empty: #If no empty cell found, puzzle is solved
        return True
    
    row, col = empty
    nums = list(range(1, N + 1))
    random.shuffle(nums)  #Shuffle numbers for randomness in generation

    for i in nums:
        if isValid(i, row, col):
            placeNumber(board, i, row, col)
            if solve(board):
                return True
            removeNumber(board, row, col) #Backtrack

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
            for j in range(N):
                print("─" * 3, end="")
                if j % M == M - 1 and j != N - 1:
                    print("┼", end="")

            print()

        for j in range(N):
            if j % M == 0 and j != 0:
                print("│", end="")
            if board[i][j] != 0:
                print(f" {board[i][j]} ", end="")
            else:
                print("   ", end="")

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
            removeNumber(board, row, col)
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

def userMove(board):
    while True:
        try:
            row = int(input(f"Enter row (0 to {N-1}): "))
            col = int(input(f"Enter column (0 to {N-1}): "))
            num = int(input(f"Enter number (1 to {N}): "))
            
            if 0 <= row < N and 0 <= col < N and 1 <= num <= N and board[row][col] == 0:
                if isValid(num, row, col):
                    placeNumber(board, num, row, col)
                    printBoard(board)
                    if findEmptyCell(board) is None:
                        print(f"Time taken to solve: {endTime - startTime:.2f} seconds")
                        print("Congratulations! You have solved the Sudoku!")
                        return
                else:
                    print("Invalid move. Try again.")
            else:
                print("Out of range or cell already filled. Try again.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

if __name__ == '__main__':
    N, M, difficulty = getUserInput()
    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]

    board = generateSudoku(difficulty)

    print("Initial unsolved board:")
    printBoard(board)
    print("\n\n")
    
    choice = input("Would you like to solve the puzzle yourself? (yes/no): ").strip().lower()

    if choice == "yes":
        startTime = time.time()
        userMove(board)

    else:
        startTime = time.time()
        solve(board)
        endTime = time.time()

        print(f"Time taken to solve: {endTime - startTime:.5f} seconds")
        printBoard(board)
