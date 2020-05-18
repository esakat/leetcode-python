import unittest
from longest_increasing_subsequence import Solution

class TestSolution(unittest.TestCase):

    def test_lengthOfLIS(self):
        input = [1,0,10,20,3,6,15,6,21,0,31,51,55,52]
        self.assertEqual(8, Solution.lengthOfLIS(self, input))