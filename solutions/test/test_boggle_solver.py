# Import to try resolve "ValueError: attempted relative import beyond top-level package", didn't work

import unittest

from ..boggle_solver import Boggle_Puzzle

class BoggleTest(unittest.TestCase):
    def test_it_finds_word(self):
        test_board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]   
        
        solver = Boggle_Puzzle(test_board)
        self.assertEqual(solver.find_word('SEED'), True)

    def test_it_does_not_find_word(self):
        test_board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]   
        
        solver = Boggle_Puzzle(test_board)
        self.assertEqual(solver.find_word('SHAY'), False)

if __name__ == '__main__':
    unittest.main()