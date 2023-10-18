This script provides a simple Sudoku game where the user can generate a Sudoku puzzle with their desired board size and difficulty level. Additionally, users can either solve the Sudoku themselves or let the script solve it for them.
Requirements

    Python 3.x

Features

    Generate Sudoku puzzles of various sizes (e.g., 4x4, 9x9, 16x16, etc.)
    Specify difficulty levels (ranging from 0 to 1, with 1 being the hardest)
    Ability for the user to solve the puzzle interactively
    Automated Sudoku solver
    Visual representation of the Sudoku board, with conflicts highlighted in red

How to Run

    Ensure you have Python 3.x installed.
    Run the script by executing the following command:
        python sudokusolver.py

Instructions

    When prompted, enter the desired board size (the input must be a perfect square number like 4, 9, 16, etc.).
    Specify the desired difficulty level (from 0 to 1). The higher the difficulty, the fewer clues you'll receive.
    An initial unsolved board will be displayed.
    Choose whether you want to solve the puzzle yourself or let the script do it for you.
        If you choose to solve it yourself, input your moves as prompted and view the updated board after each move. The game will notify you once you've successfully solved the puzzle.

Key Functions

    isValid(num, row, col): Checks if a number is valid for placement in a specific cell.
    placeNumber(board, num, row, col): Places a number in a specific cell.
    removeNumber(board, row, col): Removes a number from a specific cell.
    solve(board): Recursive function that solves the Sudoku puzzle.
    findEmptyCell(board): Finds an empty cell in the board.
    findConflicts(board): Identifies conflicting cells in the board.
    printBoard(board): Prints the Sudoku board with conflicts highlighted in red.
    generateSudoku(difficulty): Generates a Sudoku puzzle based on the specified difficulty.
    getUserInput(): Gets the board size and difficulty level from the user.
    getUserMove(): Gets the next move from the user.
    validateMove(row, col, num, board): Validates a user's move.
    userPlay(board): Allows the user to solve the Sudoku interactively.

Notes

    This game uses backtracking to solve the Sudoku puzzle.
    The game uses ANSI escape codes to highlight conflicts in red, which might not be visible on all terminals.