from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        union = [i for i in range(n)]
        
        def find_parent(parent, x):
            if parent[x] != x:
                return find_parent(parent, parent[x])
            return x
        
        def union_parent(parent, u, v):
            u = find_parent(parent, u)
            v = find_parent(parent, v)
            if u > v:
                parent[u] = v 
            else:
                parent[v] = u
        
        for u, v in edges:
            union_parent(union, u, v)
        
        return find_parent(union, source) == find_parent(union, destination)