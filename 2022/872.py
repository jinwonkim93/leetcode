# Definition for a binary tree node.
from typing import Optinonal, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def tree_traversal(root: Optional[TreeNode]) -> List:
            stack = [root]
            last_leaves = []
            while stack:
                cur_node = stack.pop()
                if cur_node.left is not None:
                    stack.append(cur_node.left)
                if cur_node.right is not None:
                    stack.append(cur_node.right)
                if cur_node.left is None and cur_node.right is None:
                    last_leaves.append(cur_node.val)
            return last_leaves
        return tree_traversal(root1) == tree_traversal(root2)