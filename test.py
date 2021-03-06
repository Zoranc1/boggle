import unittest
from string import ascii_uppercase
from  boggle import *

class TestBoggle(unittest.TestCase):
    
    def test_empty_grid(self):
        grid =make_grid(0, 0)
        self.assertEqual(grid, {})
        
    def test_non_empty_grid(self):
        grid = make_grid(2, 2)
        self.assertEqual(len(grid), 4)
        
    def test_grid_has_upper_case_letters(self):
        grid = make_grid(2, 2)
        for c in grid.values():
            self.assertIn(c, ascii_uppercase)    
    