"""This module contains functions to solve using superposition"""

# pylint: disable=trailing-newlines, too-many-arguments
import random
from copy import deepcopy
from typing import Union

import numpy as np


# Binary functions
def get_amount_of_ones(binary: Union[int, str]):
    """Get the amount of ones in a binary input"""
    if isinstance(binary, int):
        binary_string = bin(binary)[2:]
    else:
        binary_string = binary
    return sum(int(i) for i in binary_string)


def binary_to_indices(binary: Union[int, str], reverse: bool = True):
    """Convert the binary to a list of indices"""
    if isinstance(binary, int):
        binary_string = bin(binary)[2:]
    else:
        binary_string = binary
    if reverse:
        binary_string = reversed(binary_string)
    return [i + 1 for i, bit in enumerate(binary_string) if bit == "1"]


# Superposition functions
def update_board(binaries, row: int, col: int, number: int, base_size: int):
    """Update the superpositions of the grid, when a number on [rol, col] is added
    :param binaries: List of Lists with binary representation of options
    :param row: The index of the row where the number is changed
    :param col: The index of the column where the number is changed
    :param number: The value of the number in the changed cell
    :param base_size: The base_size of the grid (e.g. 3 with a 9x9 sudoku)"""

    # Create a binary with 1 on position of param: number [note that it is reversed]
    binary = list("0" * (base_size**2))
    binary[base_size**2 - number] = "1"
    out = int("".join(binary), 2)

    # Update columns and rows
    for _i in range(base_size**2):
        binaries[row][_i] &= ~out
        binaries[_i][col] &= ~out

    # Update the boxes
    starting_row = row - row % base_size
    starting_column = col - col % base_size
    for _i in range(int(base_size)):
        for _j in range(int(base_size)):
            binaries[_i + starting_row][_j + starting_column] &= ~out

    # Set binary at rol, col to be 0 (there are no options left)
    binaries[row][col] = int("0", 2)


def can_place(grid, binaries, row, col, guess, base):
    """This function returns a boolean based on the guess if the board would be unsolveable after"""
    # Save a copy of the grid, to make changes and see if it can be solved
    temp_grid = deepcopy(grid)
    temp_bin = deepcopy(binaries)

    temp_grid[row][col] = guess
    update_board(temp_bin, row, col, guess, base)

    # Check if along the line a logical problem arises ( value = 0 and bin choices = 0)
    is_zero = [1 if x.bit_length() == 0 else 0 for y in temp_bin for x in y]
    is_zero2 = [1 if x == 0 else 0 for y in temp_grid for x in y]

    for i, j in zip(is_zero, is_zero2):
        if i == 1 and j != 0:
            return False
    return True


def recursive_solve(grid, binaries, base) -> bool:
    """Recursive solving function for superposition"""
    # Step 1 : Check if the solution has been found
    if 0 not in [x for sl in grid for x in sl]:
        return True

    # Step 2 : Make a guess, based on lowest option count
    flattened_binaries = [x for y in binaries for x in y]
    index_lowest = np.argmin(
        [get_amount_of_ones(x) if x != 0 else float("inf") for x in flattened_binaries]
    )
    guess = random.choice(binary_to_indices(flattened_binaries[index_lowest]))
    row = int(index_lowest / (base**2))
    col = index_lowest % (base**2)

    # Step 3 : Save current states to reset to if needed
    save_binaries = deepcopy(binaries)
    save_grid = deepcopy(grid)

    # Step 4 : Check if the number can be placed
    if can_place(grid, binaries, row, col, guess, base):
        # Step 5 : Update the board
        update_board(binaries, row, col, guess, base)
        grid[row][col] = guess

        # Step 6 : Reiterate
        if recursive_solve(grid, binaries, base):
            return True
    else:
        # Step 7 : Reset the grid and binaries
        grid = save_grid
        binaries = save_binaries

    return False
