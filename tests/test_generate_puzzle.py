from lib.generate_puzzle import *
import unittest


class TestGeneratePuzzle(unittest.TestCase):
    def test_generate_full_board(self):
        # Test if shape is correct
        for i in [2, 3, 4, 5]:
            puzzle = Puzzle(i)
            puzzle.solution = generate_full_puzzle(i)
            assert len(puzzle.solution) == i * i

    def test_is_valid_puzzle(self):
        # Test if full grid is valid
        for i in [2, 3, 4, 5]:
            puzzle = Puzzle(i)
            puzzle.solution = generate_full_puzzle(i)
            assert validate_full_grid(puzzle) is True

    def test_generate_puzzle(self):
        # Test if generated puzzle is valid
        for i in [2, 3, 4]:
            puzzle = Puzzle(i)
            puzzle.solution = generate_full_puzzle(i)
            puzzle.board = empty_board(puzzle)
            assert puzzle.solution is not None
            assert puzzle.board is not None

            assert puzzle.board != puzzle.solution
            assert len(puzzle.board) == i * i

    def test_multiple_puzzles(self):
        # Test if multiple puzzles are generated
        for i in [2, 3, 4]:
            puzzles = generate_puzzles(6 - i, i)
            for puz in puzzles:
                self.assertIsInstance(puz, Puzzle)

    def test_empty_board(self):
        puzzle = Puzzle(3)
        puzzle.solution = generate_full_puzzle(3)
        puzzle.board = empty_board(puzzle)
        assert puzzle.board is not None
        assert puzzle.unique_solutions is None

