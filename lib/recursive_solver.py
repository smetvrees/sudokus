import copy
import math

from lib.puzzle import Puzzle

"""Contains the recursive solver"""


def solve(puzzle: Puzzle, count_unique_solutions: bool = False) -> Puzzle:
    """Main function to call the recursive solver
    :param Puzzle puzzle: the puzzle that is solved
    :param bool count_unique_solutions: if True, fills information about the solution in the Puzzle object"""
    grid = copy.deepcopy(puzzle.board)
    if count_unique_solutions:
        count = [0]
        _can_solve = recursive_solve(grid, 0, 0, size=puzzle.base_size**2, solution_count=count)
        puzzle.unique_solutions = count[0]
    _can_solve = recursive_solve(grid, 0, 0, size=puzzle.base_size**2)
    return grid


def recursive_solve(grid, row, column, size, solution_count: [int] = None) -> bool:
    # Check if we finished backtracking
    if row == size - 1 and column == size:
        if solution_count:
            solution_count[0] += 1
        return True

    # Check if end of column
    if column == size:
        row += 1
        column = 0

    # Check if this has a value. If yes; iterate next column
    if grid[row][column] > 0:
        return recursive_solve(grid, row, column + 1, size, solution_count)

    # Start the loop by trying all numbers from 1 to size
    for number in range(1, size + 1, 1):
        # Check if we can place the number
        if can_place(grid, size, row, column, number):
            # Assign number
            grid[row][column] = number

            # Iterate next column
            if recursive_solve(grid, row, column + 1, size, solution_count):
                # If solution_count is given, don't return True but reset value and iterate next column
                if solution_count:
                    grid[row][column] = 0
                    continue
                else:
                    return True

        # Placement failed; remove value and return
        grid[row][column] = 0

    return False


def can_place(grid, size, row, column, number):
    """Function that checks if a number is valid to place at grid[row][column]"""
    if number in grid[row]:
        return False

    for x in range(size):
        if grid[x][column] == number:
            return False

    base = int(math.sqrt(size))
    starting_row = row - row % base
    starting_column = column - column % base
    for i in range(int(base)):
        for j in range(int(base)):
            if grid[i + starting_row][j + starting_column] == number:
                return False

    return True
