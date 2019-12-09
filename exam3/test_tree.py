
#!/usr/bin/python3

import unittest
from tree import show_tree
from math import floor

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_tree1(self):
        self.assertEqual( show_tree(1), "x\nx")

    def test_tree2(self):
        self.assertEqual( show_tree(2), " x \nxxx\n x ")
        
    def test_tree5(self):
        self.assertEqual( show_tree(5), "  x  \n xxx \nxxxxx\n xxx \n xxx ")

    def test_tree30(self):
        self.assertEqual( show_tree(30), "")  

if __name__ == '__main__':
    unittest.main()
