"""This module contains functions to generate functions"""
import random
from copy import deepcopy
from typing import List

from tqdm import tqdm

from lib.puzzle import Puzzle
from lib.recursive_solver import recursive_solve


def generate_puzzles(amount: int, base: int) -> List[Puzzle]:
    """Generates an 'amount' of puzzles with a 'base' size"""
    output_puzzles = []
    if 1 < base < 6:
        for _i in tqdm(range(amount)):
            puzzle = Puzzle(base)
            puzzle.solution = generate_full_puzzle(base)
            puzzle.board = empty_board(puzzle)
            output_puzzles.append(puzzle)
    return output_puzzles


def generate_full_puzzle(base: int) -> List[List[int]]:
    """A funtion that with a given base (size of a box)
    creates a filled board of size [base**2 x base**2]"""
    # Based on https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
    size = base * base

    def pattern(r, c):
        return (base * (r % base) + r // base + c) % size

    def shuffle(s):
        return random.sample(s, len(s))

    base_range = range(base)
    rows = [g * base + r for g in shuffle(base_range) for r in shuffle(base_range)]
    cols = [g * base + r for g in shuffle(base_range) for r in shuffle(base_range)]

    numbers = range(1, size + 1)

    grid = [[numbers[pattern(r, c)] for c in cols] for r in rows]

    return grid


def empty_board(puzzle: Puzzle) -> Puzzle:
    """Function that will randomly pick values in a board and continues until no solution"""
    puzzle.board = deepcopy(puzzle.solution)
    size = puzzle.base_size**2

    # Start looping
    while True:
        test_count = [0]
        recursive_solve(puzzle, row=0, column=0, solution_count=test_count)

        if test_count[0] != 1:
            break

        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if puzzle.board[x][y] != 0:
            puzzle.board[x][y] = 0

    return puzzle


def validate_full_grid(puzzle: Puzzle) -> bool:
    """Returns true if the full grid is a valid sudoku"""
    base = puzzle.base_size

    # Validate Rules of Sudoku:
    for row in puzzle.solution:
        if list(dict.fromkeys(row)) != row:
            return False
    # Unique column
    for i in range(len(puzzle.solution)):
        column = [x[i] for x in puzzle.solution]
        if list(dict.fromkeys(column)) != column:
            return False
    # Unique box
    for box_index in range(puzzle.size):
        box_row = (box_index // base) * base
        box_col = (box_index % base) * base
        box_numbers = []
        for i in range(box_row, box_row + base):
            for j in range(box_col, box_col + base):
                box_numbers.append(puzzle.solution[i][j])
        if list(dict.fromkeys(box_numbers)) != box_numbers:
            return False

    return True
