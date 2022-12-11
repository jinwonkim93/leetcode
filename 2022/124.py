from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float('-inf')
        def calc_tree(node):
            if node is None: return 0
            left_sum = calc_tree(node.left)
            right_sum = calc_tree(node.right)
            single_path = max(node.val+max(left_sum, right_sum), node.val)
            result = max(single_path, node.val+left_sum+right_sum)
            self.max_val = max(self.max_val, result)
            return single_path
        calc_tree(root)
        return self.max_val