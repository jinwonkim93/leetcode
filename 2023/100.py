from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            value = []
            
            if node is not None:
                value.append(node.val)
            
                if node.left is not None:
                    value += dfs(node.left)
                else:
                    value.append(None)
                if node.right is not None:
                    value += dfs(node.right)
                else:
                    value.append(None)
            else:
                value.append(None)
            
            return value
        
        return dfs(p) == dfs(q)