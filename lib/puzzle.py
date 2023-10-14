"""This module contains the main Puzzle class"""


class Puzzle:
    """Main class that holds everything for the puzzle"""

    solution = None
    board = None
    unique_solutions = None

    def __init__(self, base_size):
        self.base_size = base_size

    def return_information(self) -> dict:
        """Return information about this puzzle"""
        return {"unique_solutions": self.unique_solutions}

    def is_board_equal_to_solution(self) -> bool:
        """Returns a boolean if board == solution"""
        if self.solution == self.board:
            return True
        return False
