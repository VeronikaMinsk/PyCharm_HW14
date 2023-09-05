import unittest
from chess import queens, generation_successful

class TestQueens(unittest.TestCase):

    def test_non_attacking_queens(self):
        queens_positions = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
        self.assertFalse(queens(queens_positions))

    def test_attacking_queens_same_row(self):
        queens_positions = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
        self.assertFalse(queens(queens_positions))

    def test_attacking_queens_same_column(self):
        queens_positions = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]
        self.assertFalse(queens(queens_positions))

    def test_attacking_queens_diagonal(self):
        queens_positions = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
        self.assertFalse(queens(queens_positions))

    def test_random_successful_arrangements(self):
        successful_arrangements = generation_successful()
        self.assertEqual(len(successful_arrangements), 4)

if __name__ == '__main__':
    unittest.main()
