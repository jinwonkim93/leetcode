# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def calc_recursive(cur, node, max_value, min_value):
            if node is not None:
                cur = max(cur, max(abs(node.val-max_value), abs(node.val-min_value)))
                max_value = max(node.val, max_value)
                min_value = min(node.val, min_value)
                cur = max(cur, calc_recursive(cur, node.left, max_value, min_value))
                cur = max(cur, calc_recursive(cur, node.right, max_value, min_value))
            return cur
        
        ans = calc_recursive(0, root, root.val, root.val)

        return ans