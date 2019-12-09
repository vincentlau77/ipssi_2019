#!/usr/bin/python3

import unittest
from sla import show_sla
from math import floor

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_sla99_9(self):
        self.assertEqual( show_sla(99.9), "8h 45m 57.0s")

    def test_sla99_8(self):
        self.assertEqual( show_sla(99.8), "17h 31m 55.0s")

    def test_sla99_5(self):
        self.assertEqual( show_sla(99.5), "43h 49m 48.0s")  

if __name__ == '__main__':
    unittest.main()
