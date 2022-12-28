from heapq import heappush, heappop, heapify
from typing import List
from math import ceil

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = []
        [heappush(heap, (-value, value)) for value in piles]
        cur_max = 0
        for _ in range(k):
            
            if len(heap) > 0 and cur_max == 0:
                _, cur_max = heappop(heap)
            else:
                if len(heap) > 0 and cur_max < heap[0][1]:
                    heappush(heap, (-cur_max, cur_max))
                    _, cur_max = heappop(heap)
                    
            cur_max = ceil(cur_max / 2)
        return sum([value[1] for value in heap])+cur_max