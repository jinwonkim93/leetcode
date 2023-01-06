from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x : x[1])
        ans = 1
        cur_end = points[0][1]
        for start, end in points:
            if start > cur_end: 
                ans += 1
                cur_end = end
        return ans