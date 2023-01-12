from typing import List
from collections import defaultdict, Counter


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        res = [0] * n
        
        def edges_to_tree(edges):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree
        
        def dfs(tree, labels, cur, parent):
            nonlocal res
            ans = Counter()
            for next_node in tree[cur]:
                if next_node != parent:
                    ans += dfs(tree, labels, next_node, cur)
                
            ans[ord(labels[cur])] += 1
            res[cur] =  ans[ord(labels[cur])]
                
            return ans
        
        tree = edges_to_tree(edges)
        dfs(tree, list(labels), 0, -1)
        return res