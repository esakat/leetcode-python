import unittest
from convert_sorted_array_to_binary_search_tree import Solution
from algorithm.treenode import TreeNode

class TestSolution(unittest.TestCase):

    def test_sortedArrayToBST(self):
        input = [-10, -3, 0, 5, 9]
        root = TreeNode(0)
        root.left = TreeNode(-3)
        root.right = TreeNode(9)
        root.left.left = TreeNode(-10)
        root.right.left = TreeNode(5)
        self.assertEqual(root.val, Solution.sortedArrayToBST(self, input).val)