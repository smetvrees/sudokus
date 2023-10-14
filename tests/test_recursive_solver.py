"""Test module for the recursive solver"""
import unittest

from lib.recursive_solver import recursive_solve, solve, can_place
from tests.puzzles import PuzzleTest


class TestRecursiveSolver(unittest.TestCase):
    """Test class for recursive solve"""
    def test_can_place(self):
        """Test if can_place returns booleans properly"""
        puzzle = PuzzleTest(3)

        assert can_place(puzzle.board, 9, 0, 1, 2) is False  # Check column
        assert can_place(puzzle.board, 9, 2, 0, 6) is False  # Check box
        assert can_place(puzzle.board, 9, 3, 3, 7) is True  # Check all
        assert can_place(puzzle.board, 9, 8, 8, 3) is False  # Check row

    def test_solutions(self):
        """Test if this puzzle has 1 unique solution"""
        for base in [2, 3, 4]:
            puzzle = PuzzleTest(base)
            solution = solve(puzzle, True)
            assert puzzle.unique_solutions == 1
            assert puzzle.solution == solution

    def test_count_solutions(self):
        """Test if recursive solver produces the right amount of solutions"""
        amounts = [0]
        recursive_solve([[0] * 4] * 4, 0, 0, size=4, solution_count=amounts)
        assert amounts == [24]
        amounts = [0]
        recursive_solve([[0] * 9] * 9, 0, 0, size=9, solution_count=amounts)
        assert amounts == [362880]
