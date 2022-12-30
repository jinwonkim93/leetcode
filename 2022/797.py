from typing import List
from collections import defaultdict

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        graph_dict = defaultdict(list)
        ans = []
        for idx, nodes in enumerate(graph):
            graph_dict[idx].extend(nodes)

        queue = [(0, 0)]
        possible_path = []
        while queue:
            cur_node, level = queue.pop()
            possible_path = possible_path[:level] + [cur_node]
            next_nodes = graph_dict[cur_node]
            for node in next_nodes:
                queue.append((node, level+1))
            
            if cur_node == len(graph)-1:
                ans.append(possible_path)
        return ans