from typing import List
from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        
        def dfs(node, hasApple, key, parent):
            ans = 0

            for sub_node in node[key]:
                if sub_node != parent:
                    ans += dfs(node, hasApple, sub_node, key)
            
            if parent != -1 and (ans > 0 or hasApple[key] is True):
                ans += 2
                
            return ans
        
        def make_node(edges):
            
            node = defaultdict(list)
            for u, v in edges:
                node[u].append(v)
                node[v].append(u)
            return node
        
        node = make_node(edges)
        return dfs(node, hasApple,  0, -1)