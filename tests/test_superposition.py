"""Testing module for superposition solve"""
import unittest
from copy import deepcopy
from lib.generate_puzzle import validate_full_grid
from lib.superposition_solve import (binary_to_indices, can_place,
                                     recursive_solve, update_board)
from tests.puzzles import PuzzleTest


class TestSuperPosition(unittest.TestCase):
    """Test class for testing the superposition solve"""
    def test_binary_to_indices(self):
        """Test if binary to indices is working properly"""
        assert binary_to_indices(13) == [1, 3, 4]
        assert binary_to_indices("010101") == [1, 3, 5]
        assert binary_to_indices("10") == [2]

    def test_update_board(self):
        """Test if the update board function is working properly"""
        base = 2
        base_bin = [int("1" * (base**2), 2)]
        binaries = [base_bin * (base**2) for _ in range((base**2))]

        assert binaries == [
            [15, 15, 15, 15],
            [15, 15, 15, 15],
            [15, 15, 15, 15],
            [15, 15, 15, 15],
        ]

        update_board(binaries, 1, 1, 2, 2)

        assert binaries == [
            [13, 13, 15, 15],
            [13, 0, 13, 13],
            [15, 13, 15, 15],
            [15, 13, 15, 15],
        ]

        update_board(binaries, 3, 2, 4, 2)

        assert binaries == [
            [13, 13, 7, 15],
            [13, 0, 5, 13],
            [15, 13, 7, 7],
            [7, 5, 0, 7],
        ]

    def test_can_place(self):
        """Test if can place function is working properly"""
        base = 2
        puzzle = PuzzleTest(base)

        base_bin = [int("1" * (base**2), 2)]
        binaries = [base_bin * (base**2) for _ in range((base**2))]
        solve_puzzle = deepcopy(puzzle.board)

        for i, row in enumerate(solve_puzzle):
            for j, item in enumerate(row):
                if item != 0:
                    update_board(binaries, i, j, item, base)

        assert can_place(puzzle.board, binaries, 0, 0, 2, 2) is False
        assert can_place(puzzle.board, binaries, 0, 1, 4, 2) is True
        assert can_place(puzzle.board, binaries, 3, 0, 4, 2) is True
        assert can_place(puzzle.board, binaries, 1, 2, 2, 2) is False

    def test_solve_superposition(self):
        """Test if the solve returns a valid solution"""
        for base in [2, 3, 4]:
            puzzle = PuzzleTest(base)

            # Set up the board and update binaries
            base_bin = [int("1" * (base**2), 2)]
            binaries = [base_bin * (base**2) for _ in range((base**2))]
            solve_puzzle = deepcopy(puzzle.board)

            for i, row in enumerate(solve_puzzle):
                for j, item in enumerate(row):
                    if item != 0:
                        update_board(binaries, i, j, item, base)

            # Setup the recursion
            recursive_solve(puzzle.board, binaries, base)

            assert validate_full_grid(puzzle) is True
