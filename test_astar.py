import unittest
from astar import a_star_search

class TestAStar(unittest.TestCase):
    def test_simple_path(self):
        grid = [
            ['.', '.', '.'],
            ['#', '#', '.'],
            ['.', '.', '.']
        ]
        start = (0, 0)
        goal = (2, 2)
        path = a_star_search(grid, start, goal)
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])

    def test_no_path(self):
        grid = [
            ['.', '.', '.'],
            ['#', '#', '#'],
            ['.', '.', '.']
        ]
        start = (0, 0)
        goal = (2, 2)
        path = a_star_search(grid, start, goal)
        self.assertIsNone(path)

if __name__ == '__main__':
    unittest.main()