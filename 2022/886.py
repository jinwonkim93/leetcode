from typing import List
from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        group = [-1] * n
        connection = defaultdict(list)
        for a, b in dislikes:
            connection[a-1].append(b-1)
            connection[b-1].append(a-1)
        
        for i in range(n):
            if group[i] != -1: continue
            q = [i]
            cur_groups = [0]
            while q:
                cur = q.pop()
                cur_group = cur_groups.pop()
                group[cur] = cur_group
                for dislike_node in connection[cur]:
                    if group[dislike_node] == group[cur]: return False
                    if group[dislike_node] == -1:
                        q.append(dislike_node)
                        cur_groups.append(1 - cur_group)
        return True
        
        