import unittest
from best_time_to_buy_and_sell_stock_ii import Solution

class TestSolution(unittest.TestCase):

    def test_maxProfit(self):
        input = [7,1,5,3,6,4]
        ans = 7
        self.assertEqual(ans, Solution.maxProfit(self, input))

        input = [1,2,3,4,5]
        ans = 4
        self.assertEqual(ans, Solution.maxProfit(self, input))

        input = [7,6,4,3,1]
        ans = 0
        self.assertEqual(ans, Solution.maxProfit(self, input))
