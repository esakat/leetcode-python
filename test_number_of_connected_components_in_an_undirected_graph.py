import unittest
from number_of_connected_components_in_an_undirected_graph import Solution

class TestSolution(unittest.TestCase):

    def test_countComponents(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        expected = 1
        self.assertEqual(expected, Solution.countComponents(self, n, edges))