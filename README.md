# Sudoku-Solver

Introduction

This program provides an implementation of a Sudoku puzzle generator and solver. Users can specify the size of the board, with common sizes being 4x4, 9x9, 16x16, and so on. The board size must be a perfect square. In addition, users can also set the difficulty level of the generated puzzle. The difficulty determines the number of initial filled cells in the puzzle.
Features

    Board Size Customization: Users can select the size of the Sudoku board.
    Difficulty Levels: Allows users to set the difficulty of the Sudoku puzzles.
    Sudoku Generator: Generates a random Sudoku puzzle based on the specified size and difficulty.
    Sudoku Solver: Solves any given valid Sudoku puzzle.

Functions
isValid(board, row, col, num)

    Parameters:
        board: Current state of the Sudoku board.
        row, col: Position on the board to check.
        num: Number to validate.
    Return: Returns True if the number num can be placed at the given row and col without violating Sudoku rules, otherwise False.

solve(board)

    Parameter:
        board: Current state of the Sudoku board.
    Return: Returns True if the Sudoku puzzle can be solved, otherwise False.

findEmptyCell(board)

    Parameter:
        board: Current state of the Sudoku board.
    Return: Returns the coordinates (row, col) of the first empty cell (with value 0) found, or None if no empty cells are found.

printBoard(board)

    Parameter:
        board: Current state of the Sudoku board.
    Action: Prints the board in a human-readable format.

generateSudoku(difficulty=0.5)

    Parameter:
        difficulty: Proportion of cells to be emptied. Value between 0 and 1, where 1 means all cells will be emptied.
    Return: Returns a generated Sudoku board based on the given difficulty.

getUserInput()

    Return: Gets board size and difficulty from the user and returns these values as (N, M, difficulty).

How to Use

    Run the program.
    Input the desired board size (e.g., 9 for a 9x9 board). Note: The size must be a perfect square.
    Input the desired difficulty level (between 0 and 1). The closer to 1, the harder the puzzle.
    The program will display an initial unsolved board.
    The program will then solve the puzzle and display the solution.
