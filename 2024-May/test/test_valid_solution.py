import unittest

from src.grid import Grid


class TestValidSolution(unittest.TestCase):
    def test_correct(self):
        grid = Grid('src/small.csv')
        solution = [
            [-1, 3, 4, 3, -1],
            [1, 3, -1, 5, 5],
            [1, 3, 7, 7, 5],
            [-1, 3, 3, 7, 5],
            [7, 3, 3, 7, -1]
        ]
        grid.table = solution
        self.assertTrue(grid.valid_solution())

    def test_incorrect(self):
        grid = Grid('src/small.csv')
        incorrect_solution = [
            [-1, 3, 4, 3, -1],
            [1, 3, -1, 5, 5],
            [1, 3, 7, 7, 6],
            [-1, 3, 3, 7, 5],
            [7, 3, 3, 7, -1]
        ]
        grid.table = incorrect_solution
        self.assertFalse(grid.valid_solution())


if __name__ == '__main__':
    unittest.main()
