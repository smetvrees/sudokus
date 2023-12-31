"""Module that creates a Puzzle object with built-in problems"""
# pylint: disable=too-many-lines, line-too-long

from lib.puzzle import Puzzle


class PuzzleTest(Puzzle):
    """Inherits from puzzle and overrides board and solution with valid puzzles for testing"""

    def __init__(self, base_size):
        super().__init__(base_size)
        self.base_size = base_size
        self.unique_solutions = None
        if base_size == 2:
            self.solution = [[1, 4, 3, 2], [3, 2, 1, 4], [2, 1, 4, 3], [4, 3, 2, 1]]
            self.board = [[1, 0, 0, 0], [3, 0, 0, 4], [2, 0, 0, 0], [0, 3, 0, 1]]
        elif base_size == 3:
            self.board = [
                [3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0],
            ]
            self.solution = [
                [3, 1, 6, 5, 7, 8, 4, 9, 2],
                [5, 2, 9, 1, 3, 4, 7, 6, 8],
                [4, 8, 7, 6, 2, 9, 5, 3, 1],
                [2, 6, 3, 4, 1, 5, 9, 8, 7],
                [9, 7, 4, 8, 6, 3, 1, 2, 5],
                [8, 5, 1, 7, 9, 2, 6, 4, 3],
                [1, 3, 8, 9, 4, 7, 2, 5, 6],
                [6, 9, 2, 3, 5, 1, 8, 7, 4],
                [7, 4, 5, 2, 8, 6, 3, 1, 9],
            ]
        elif base_size == 4:
            self.board = [
                [0, 0, 7, 9, 0, 0, 1, 2, 0, 4, 6, 5, 13, 14, 12, 0],
                [6, 4, 3, 5, 12, 11, 13, 14, 15, 16, 0, 1, 9, 10, 8, 7],
                [0, 16, 15, 1, 8, 7, 9, 10, 11, 12, 14, 13, 5, 0, 4, 3],
                [14, 0, 11, 13, 0, 3, 5, 6, 7, 8, 10, 0, 1, 2, 16, 15],
                [0, 9, 8, 10, 1, 16, 0, 3, 4, 5, 7, 6, 14, 15, 13, 12],
                [3, 1, 16, 0, 9, 8, 10, 0, 12, 13, 15, 14, 6, 0, 5, 4],
                [0, 5, 0, 6, 13, 12, 14, 15, 16, 1, 3, 0, 0, 11, 9, 8],
                [15, 13, 0, 14, 5, 4, 6, 7, 8, 9, 11, 10, 0, 3, 1, 0],
                [0, 10, 0, 11, 0, 1, 3, 4, 5, 6, 8, 7, 15, 0, 14, 13],
                [0, 0, 5, 7, 14, 13, 0, 16, 0, 2, 4, 3, 11, 12, 0, 9],
                [4, 2, 0, 0, 10, 9, 0, 12, 13, 14, 16, 15, 0, 8, 6, 5],
                [16, 14, 13, 15, 6, 5, 7, 8, 9, 10, 12, 11, 0, 4, 0, 0],
                [0, 3, 0, 0, 11, 10, 12, 13, 14, 0, 1, 0, 8, 9, 7, 6],
                [0, 11, 10, 12, 3, 2, 4, 0, 6, 7, 9, 8, 0, 1, 0, 14],
                [9, 7, 6, 8, 0, 14, 16, 0, 2, 0, 5, 0, 12, 0, 0, 10],
                [1, 15, 14, 16, 0, 6, 8, 9, 10, 0, 0, 0, 4, 5, 0, 2],
            ]
            self.solution = [
                [10, 8, 7, 9, 16, 15, 1, 2, 3, 4, 6, 5, 13, 14, 12, 11],
                [6, 4, 3, 5, 12, 11, 13, 14, 15, 16, 2, 1, 9, 10, 8, 7],
                [2, 16, 15, 1, 8, 7, 9, 10, 11, 12, 14, 13, 5, 6, 4, 3],
                [14, 12, 11, 13, 4, 3, 5, 6, 7, 8, 10, 9, 1, 2, 16, 15],
                [11, 9, 8, 10, 1, 16, 2, 3, 4, 5, 7, 6, 14, 15, 13, 12],
                [3, 1, 16, 2, 9, 8, 10, 11, 12, 13, 15, 14, 6, 7, 5, 4],
                [7, 5, 4, 6, 13, 12, 14, 15, 16, 1, 3, 2, 10, 11, 9, 8],
                [15, 13, 12, 14, 5, 4, 6, 7, 8, 9, 11, 10, 2, 3, 1, 16],
                [12, 10, 9, 11, 2, 1, 3, 4, 5, 6, 8, 7, 15, 16, 14, 13],
                [8, 6, 5, 7, 14, 13, 15, 16, 1, 2, 4, 3, 11, 12, 10, 9],
                [4, 2, 1, 3, 10, 9, 11, 12, 13, 14, 16, 15, 7, 8, 6, 5],
                [16, 14, 13, 15, 6, 5, 7, 8, 9, 10, 12, 11, 3, 4, 2, 1],
                [5, 3, 2, 4, 11, 10, 12, 13, 14, 15, 1, 16, 8, 9, 7, 6],
                [13, 11, 10, 12, 3, 2, 4, 5, 6, 7, 9, 8, 16, 1, 15, 14],
                [9, 7, 6, 8, 15, 14, 16, 1, 2, 3, 5, 4, 12, 13, 11, 10],
                [1, 15, 14, 16, 7, 6, 8, 9, 10, 11, 13, 12, 4, 5, 3, 2],
            ]

        elif base_size == 5:
            self.solution = [
                [
                    12,
                    13,
                    10,
                    0,
                    14,
                    0,
                    0,
                    0,
                    25,
                    3,
                    20,
                    0,
                    24,
                    0,
                    21,
                    0,
                    5,
                    9,
                    6,
                    8,
                    0,
                    16,
                    19,
                    18,
                    15,
                ],
                [
                    22,
                    0,
                    20,
                    0,
                    24,
                    14,
                    11,
                    12,
                    10,
                    13,
                    5,
                    7,
                    0,
                    8,
                    6,
                    0,
                    0,
                    19,
                    16,
                    18,
                    2,
                    1,
                    4,
                    3,
                    25,
                ],
                [
                    17,
                    0,
                    15,
                    16,
                    19,
                    9,
                    6,
                    0,
                    5,
                    8,
                    25,
                    0,
                    0,
                    0,
                    1,
                    0,
                    10,
                    14,
                    0,
                    13,
                    0,
                    0,
                    24,
                    0,
                    20,
                ],
                [
                    0,
                    3,
                    0,
                    0,
                    4,
                    19,
                    0,
                    17,
                    15,
                    18,
                    10,
                    12,
                    14,
                    13,
                    0,
                    22,
                    20,
                    0,
                    21,
                    23,
                    7,
                    6,
                    9,
                    8,
                    5,
                ],
                [
                    7,
                    8,
                    5,
                    0,
                    9,
                    24,
                    0,
                    0,
                    0,
                    23,
                    15,
                    17,
                    19,
                    18,
                    16,
                    0,
                    25,
                    0,
                    1,
                    0,
                    0,
                    11,
                    14,
                    0,
                    10,
                ],
                [
                    15,
                    16,
                    13,
                    14,
                    17,
                    0,
                    4,
                    5,
                    3,
                    6,
                    23,
                    25,
                    2,
                    0,
                    0,
                    10,
                    0,
                    0,
                    9,
                    11,
                    20,
                    19,
                    0,
                    0,
                    18,
                ],
                [
                    20,
                    21,
                    18,
                    0,
                    22,
                    12,
                    9,
                    10,
                    8,
                    0,
                    3,
                    0,
                    0,
                    6,
                    4,
                    15,
                    13,
                    17,
                    14,
                    16,
                    0,
                    0,
                    0,
                    1,
                    23,
                ],
                [
                    5,
                    6,
                    3,
                    4,
                    0,
                    0,
                    19,
                    20,
                    18,
                    21,
                    0,
                    0,
                    17,
                    0,
                    14,
                    25,
                    23,
                    0,
                    0,
                    1,
                    10,
                    9,
                    12,
                    11,
                    8,
                ],
                [
                    25,
                    1,
                    23,
                    24,
                    0,
                    17,
                    14,
                    15,
                    13,
                    16,
                    8,
                    10,
                    12,
                    11,
                    0,
                    0,
                    18,
                    0,
                    19,
                    21,
                    0,
                    4,
                    7,
                    6,
                    3,
                ],
                [
                    0,
                    11,
                    8,
                    0,
                    12,
                    0,
                    24,
                    25,
                    23,
                    0,
                    0,
                    20,
                    22,
                    21,
                    0,
                    5,
                    3,
                    7,
                    4,
                    6,
                    0,
                    14,
                    0,
                    0,
                    13,
                ],
                [
                    24,
                    0,
                    0,
                    0,
                    0,
                    0,
                    13,
                    14,
                    12,
                    15,
                    7,
                    9,
                    11,
                    0,
                    8,
                    0,
                    0,
                    21,
                    18,
                    20,
                    4,
                    3,
                    6,
                    5,
                    0,
                ],
                [
                    14,
                    15,
                    0,
                    13,
                    16,
                    6,
                    0,
                    4,
                    2,
                    5,
                    22,
                    0,
                    1,
                    25,
                    23,
                    9,
                    0,
                    11,
                    8,
                    0,
                    19,
                    0,
                    21,
                    20,
                    17,
                ],
                [
                    9,
                    10,
                    7,
                    0,
                    11,
                    0,
                    0,
                    0,
                    0,
                    25,
                    17,
                    19,
                    21,
                    0,
                    0,
                    4,
                    2,
                    0,
                    3,
                    5,
                    14,
                    13,
                    16,
                    15,
                    12,
                ],
                [
                    4,
                    5,
                    2,
                    3,
                    0,
                    0,
                    18,
                    19,
                    0,
                    20,
                    12,
                    0,
                    16,
                    15,
                    0,
                    24,
                    0,
                    0,
                    0,
                    25,
                    9,
                    8,
                    0,
                    0,
                    7,
                ],
                [
                    19,
                    20,
                    17,
                    18,
                    21,
                    11,
                    8,
                    9,
                    7,
                    10,
                    0,
                    4,
                    6,
                    5,
                    0,
                    14,
                    12,
                    16,
                    13,
                    15,
                    24,
                    23,
                    1,
                    25,
                    22,
                ],
                [
                    1,
                    0,
                    24,
                    25,
                    0,
                    18,
                    15,
                    16,
                    14,
                    0,
                    9,
                    11,
                    13,
                    0,
                    10,
                    21,
                    19,
                    23,
                    20,
                    22,
                    6,
                    5,
                    8,
                    7,
                    4,
                ],
                [
                    16,
                    17,
                    0,
                    0,
                    18,
                    0,
                    5,
                    6,
                    4,
                    7,
                    0,
                    1,
                    0,
                    0,
                    25,
                    11,
                    0,
                    13,
                    0,
                    12,
                    21,
                    20,
                    0,
                    22,
                    0,
                ],
                [
                    11,
                    12,
                    0,
                    10,
                    13,
                    3,
                    25,
                    1,
                    24,
                    2,
                    0,
                    21,
                    23,
                    22,
                    20,
                    6,
                    0,
                    0,
                    0,
                    7,
                    0,
                    15,
                    0,
                    17,
                    14,
                ],
                [
                    6,
                    7,
                    4,
                    5,
                    8,
                    23,
                    0,
                    21,
                    19,
                    22,
                    14,
                    16,
                    18,
                    0,
                    15,
                    0,
                    24,
                    3,
                    25,
                    2,
                    11,
                    0,
                    13,
                    0,
                    9,
                ],
                [
                    21,
                    0,
                    0,
                    20,
                    23,
                    13,
                    10,
                    0,
                    9,
                    12,
                    4,
                    6,
                    0,
                    0,
                    0,
                    16,
                    14,
                    18,
                    15,
                    0,
                    1,
                    25,
                    3,
                    2,
                    24,
                ],
                [
                    0,
                    0,
                    0,
                    0,
                    10,
                    25,
                    0,
                    23,
                    0,
                    24,
                    16,
                    0,
                    0,
                    19,
                    17,
                    3,
                    0,
                    5,
                    2,
                    4,
                    0,
                    0,
                    15,
                    14,
                    11,
                ],
                [
                    23,
                    24,
                    0,
                    22,
                    25,
                    0,
                    12,
                    13,
                    11,
                    14,
                    0,
                    0,
                    10,
                    9,
                    0,
                    18,
                    16,
                    20,
                    0,
                    19,
                    3,
                    2,
                    5,
                    0,
                    1,
                ],
                [
                    0,
                    0,
                    0,
                    2,
                    0,
                    20,
                    17,
                    18,
                    16,
                    19,
                    11,
                    0,
                    15,
                    14,
                    0,
                    23,
                    21,
                    25,
                    0,
                    24,
                    0,
                    7,
                    0,
                    9,
                    0,
                ],
                [
                    13,
                    0,
                    11,
                    0,
                    15,
                    0,
                    2,
                    0,
                    1,
                    4,
                    21,
                    23,
                    25,
                    24,
                    0,
                    8,
                    6,
                    10,
                    7,
                    9,
                    0,
                    0,
                    20,
                    19,
                    16,
                ],
                [
                    18,
                    0,
                    16,
                    17,
                    20,
                    0,
                    0,
                    8,
                    0,
                    9,
                    1,
                    0,
                    0,
                    4,
                    2,
                    0,
                    11,
                    0,
                    12,
                    14,
                    23,
                    22,
                    0,
                    0,
                    0,
                ],
            ]
            self.board = [
                [
                    12,
                    13,
                    10,
                    11,
                    14,
                    4,
                    1,
                    2,
                    25,
                    3,
                    20,
                    22,
                    24,
                    23,
                    21,
                    7,
                    5,
                    9,
                    6,
                    8,
                    17,
                    16,
                    19,
                    18,
                    15,
                ],
                [
                    22,
                    23,
                    20,
                    21,
                    24,
                    14,
                    11,
                    12,
                    10,
                    13,
                    5,
                    7,
                    9,
                    8,
                    6,
                    17,
                    15,
                    19,
                    16,
                    18,
                    2,
                    1,
                    4,
                    3,
                    25,
                ],
                [
                    17,
                    18,
                    15,
                    16,
                    19,
                    9,
                    6,
                    7,
                    5,
                    8,
                    25,
                    2,
                    4,
                    3,
                    1,
                    12,
                    10,
                    14,
                    11,
                    13,
                    22,
                    21,
                    24,
                    23,
                    20,
                ],
                [
                    2,
                    3,
                    25,
                    1,
                    4,
                    19,
                    16,
                    17,
                    15,
                    18,
                    10,
                    12,
                    14,
                    13,
                    11,
                    22,
                    20,
                    24,
                    21,
                    23,
                    7,
                    6,
                    9,
                    8,
                    5,
                ],
                [
                    7,
                    8,
                    5,
                    6,
                    9,
                    24,
                    21,
                    22,
                    20,
                    23,
                    15,
                    17,
                    19,
                    18,
                    16,
                    2,
                    25,
                    4,
                    1,
                    3,
                    12,
                    11,
                    14,
                    13,
                    10,
                ],
                [
                    15,
                    16,
                    13,
                    14,
                    17,
                    7,
                    4,
                    5,
                    3,
                    6,
                    23,
                    25,
                    2,
                    1,
                    24,
                    10,
                    8,
                    12,
                    9,
                    11,
                    20,
                    19,
                    22,
                    21,
                    18,
                ],
                [
                    20,
                    21,
                    18,
                    19,
                    22,
                    12,
                    9,
                    10,
                    8,
                    11,
                    3,
                    5,
                    7,
                    6,
                    4,
                    15,
                    13,
                    17,
                    14,
                    16,
                    25,
                    24,
                    2,
                    1,
                    23,
                ],
                [
                    5,
                    6,
                    3,
                    4,
                    7,
                    22,
                    19,
                    20,
                    18,
                    21,
                    13,
                    15,
                    17,
                    16,
                    14,
                    25,
                    23,
                    2,
                    24,
                    1,
                    10,
                    9,
                    12,
                    11,
                    8,
                ],
                [
                    25,
                    1,
                    23,
                    24,
                    2,
                    17,
                    14,
                    15,
                    13,
                    16,
                    8,
                    10,
                    12,
                    11,
                    9,
                    20,
                    18,
                    22,
                    19,
                    21,
                    5,
                    4,
                    7,
                    6,
                    3,
                ],
                [
                    10,
                    11,
                    8,
                    9,
                    12,
                    2,
                    24,
                    25,
                    23,
                    1,
                    18,
                    20,
                    22,
                    21,
                    19,
                    5,
                    3,
                    7,
                    4,
                    6,
                    15,
                    14,
                    17,
                    16,
                    13,
                ],
                [
                    24,
                    25,
                    22,
                    23,
                    1,
                    16,
                    13,
                    14,
                    12,
                    15,
                    7,
                    9,
                    11,
                    10,
                    8,
                    19,
                    17,
                    21,
                    18,
                    20,
                    4,
                    3,
                    6,
                    5,
                    2,
                ],
                [
                    14,
                    15,
                    12,
                    13,
                    16,
                    6,
                    3,
                    4,
                    2,
                    5,
                    22,
                    24,
                    1,
                    25,
                    23,
                    9,
                    7,
                    11,
                    8,
                    10,
                    19,
                    18,
                    21,
                    20,
                    17,
                ],
                [
                    9,
                    10,
                    7,
                    8,
                    11,
                    1,
                    23,
                    24,
                    22,
                    25,
                    17,
                    19,
                    21,
                    20,
                    18,
                    4,
                    2,
                    6,
                    3,
                    5,
                    14,
                    13,
                    16,
                    15,
                    12,
                ],
                [
                    4,
                    5,
                    2,
                    3,
                    6,
                    21,
                    18,
                    19,
                    17,
                    20,
                    12,
                    14,
                    16,
                    15,
                    13,
                    24,
                    22,
                    1,
                    23,
                    25,
                    9,
                    8,
                    11,
                    10,
                    7,
                ],
                [
                    19,
                    20,
                    17,
                    18,
                    21,
                    11,
                    8,
                    9,
                    7,
                    10,
                    2,
                    4,
                    6,
                    5,
                    3,
                    14,
                    12,
                    16,
                    13,
                    15,
                    24,
                    23,
                    1,
                    25,
                    22,
                ],
                [
                    1,
                    2,
                    24,
                    25,
                    3,
                    18,
                    15,
                    16,
                    14,
                    17,
                    9,
                    11,
                    13,
                    12,
                    10,
                    21,
                    19,
                    23,
                    20,
                    22,
                    6,
                    5,
                    8,
                    7,
                    4,
                ],
                [
                    16,
                    17,
                    14,
                    15,
                    18,
                    8,
                    5,
                    6,
                    4,
                    7,
                    24,
                    1,
                    3,
                    2,
                    25,
                    11,
                    9,
                    13,
                    10,
                    12,
                    21,
                    20,
                    23,
                    22,
                    19,
                ],
                [
                    11,
                    12,
                    9,
                    10,
                    13,
                    3,
                    25,
                    1,
                    24,
                    2,
                    19,
                    21,
                    23,
                    22,
                    20,
                    6,
                    4,
                    8,
                    5,
                    7,
                    16,
                    15,
                    18,
                    17,
                    14,
                ],
                [
                    6,
                    7,
                    4,
                    5,
                    8,
                    23,
                    20,
                    21,
                    19,
                    22,
                    14,
                    16,
                    18,
                    17,
                    15,
                    1,
                    24,
                    3,
                    25,
                    2,
                    11,
                    10,
                    13,
                    12,
                    9,
                ],
                [
                    21,
                    22,
                    19,
                    20,
                    23,
                    13,
                    10,
                    11,
                    9,
                    12,
                    4,
                    6,
                    8,
                    7,
                    5,
                    16,
                    14,
                    18,
                    15,
                    17,
                    1,
                    25,
                    3,
                    2,
                    24,
                ],
                [
                    8,
                    9,
                    6,
                    7,
                    10,
                    25,
                    22,
                    23,
                    21,
                    24,
                    16,
                    18,
                    20,
                    19,
                    17,
                    3,
                    1,
                    5,
                    2,
                    4,
                    13,
                    12,
                    15,
                    14,
                    11,
                ],
                [
                    23,
                    24,
                    21,
                    22,
                    25,
                    15,
                    12,
                    13,
                    11,
                    14,
                    6,
                    8,
                    10,
                    9,
                    7,
                    18,
                    16,
                    20,
                    17,
                    19,
                    3,
                    2,
                    5,
                    4,
                    1,
                ],
                [
                    3,
                    4,
                    1,
                    2,
                    5,
                    20,
                    17,
                    18,
                    16,
                    19,
                    11,
                    13,
                    15,
                    14,
                    12,
                    23,
                    21,
                    25,
                    22,
                    24,
                    8,
                    7,
                    10,
                    9,
                    6,
                ],
                [
                    13,
                    14,
                    11,
                    12,
                    15,
                    5,
                    2,
                    3,
                    1,
                    4,
                    21,
                    23,
                    25,
                    24,
                    22,
                    8,
                    6,
                    10,
                    7,
                    9,
                    18,
                    17,
                    20,
                    19,
                    16,
                ],
                [
                    18,
                    19,
                    16,
                    17,
                    20,
                    10,
                    7,
                    8,
                    6,
                    9,
                    1,
                    3,
                    5,
                    4,
                    2,
                    13,
                    11,
                    15,
                    12,
                    14,
                    23,
                    22,
                    25,
                    24,
                    21,
                ],
            ]
