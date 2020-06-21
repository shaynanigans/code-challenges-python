import unittest

from ..sudoku_solver import Sudoku_Puzzle

class SudokuTest(unittest.TestCase):
    def test_solve_puzzle(self):
        # TODO: Write test case to validate functionality
        test_puzzle=[
            [5,3,'.','.',7,'.','.','.','.'],
            [6,'.','.',1,9,5,'.','.','.'],
            ['.',9,8,'.','.','.','.',6,'.'],
            [8,'.','.','.',6,'.','.','.',3],
            [4,'.','.',8,'.',3,'.','.',1],
            [7,'.','.','.',2,'.','.','.',6],
            ['.',6,'.','.','.','.',2,8,'.'],
            ['.','.','.',4,1,9,'.','.',5],
            ['.','.','.','.',8,'.','.',7,9]
        ]

        puzzle = Sudoku_Puzzle(test_puzzle)
        puzzle.solve_puzzle()

        # Ran out of time writing this test case
        pass

if __name__ == '__main__':
    unittest.main()