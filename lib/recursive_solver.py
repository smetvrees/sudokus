"""This module contains functions to recursively solve"""
from lib.puzzle import Puzzle


def solve(puzzle: Puzzle, count_unique_solutions: bool = False) -> Puzzle:
    """Main function to call the recursive solver
    :param Puzzle puzzle: the puzzle that is solved
    :param bool count_unique_solutions:
        if True, fills information about the solution in the Puzzle object
    """
    if count_unique_solutions:
        count = [0]
        _can_solve = recursive_solve(puzzle, 0, 0, solution_count=count)
        puzzle.unique_solutions = count[0]
    _can_solve = recursive_solve(puzzle, 0, 0)
    return puzzle


def recursive_solve(
    puzzle: Puzzle, row: int, column: int, solution_count: [int] = None
) -> bool:
    """Recursively solve the grid"""
    # Check if we finished backtracking
    if row == puzzle.size - 1 and column == puzzle.size:
        if solution_count:
            solution_count[0] += 1
        return True

    # Check if end of column
    if column == puzzle.size:
        row += 1
        column = 0

    # Check if this has a value. If yes; iterate next column
    if puzzle.board[row][column] > 0:
        return recursive_solve(puzzle, row, column + 1, solution_count)

    # Start the loop by trying all numbers from 1 to size
    for number in range(1, puzzle.size + 1, 1):
        # Check if we can place the number
        if can_place(puzzle, row, column, number):
            # Assign number
            puzzle.board[row][column] = number

            # Iterate next column
            if recursive_solve(puzzle, row, column + 1, solution_count):
                # If solution_count is given, don't return True but reset value
                if solution_count:
                    puzzle.board[row][column] = 0
                    continue
                return True

        # Placement failed; remove value and return
        puzzle.board[row][column] = 0

    return False


def can_place(puzzle, row, column, number):
    """Function that checks if a number is valid to place at grid[row][column]"""
    if number in puzzle.board[row]:
        return False

    for x in range(puzzle.size):
        if puzzle.board[x][column] == number:
            return False

    starting_row = row - row % puzzle.base_size
    starting_column = column - column % puzzle.base_size
    for i in range(int(puzzle.base_size)):
        for j in range(int(puzzle.base_size)):
            if puzzle.board[i + starting_row][j + starting_column] == number:
                return False

    return True
