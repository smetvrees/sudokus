class Puzzle:
    """Main class that holds everything for the puzzle"""
    solution = None
    board = None
    unique_solutions = None

    def __init__(self, base_size):
        self.base_size = base_size
