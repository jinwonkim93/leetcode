from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.m = 1000000007
        self.sums = []
        def calc_tree(node):
            if node is None: return 0
            sub_tree_sum = node.val + calc_tree(node.left) + calc_tree(node.right)
            self.sums.append(sub_tree_sum)
            return sub_tree_sum
        
        total = calc_tree(root)
        result = 0
        for sum in self.sums:
            result = max(result, sum*(total-sum))
        return result%self.m