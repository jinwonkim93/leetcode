from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        need_rocks = sorted([cap - rock for cap, rock in zip(capacity, rocks)])
        answer = 0
        for need_rock in need_rocks:
            if need_rock <= additionalRocks:
                additionalRocks -= need_rock
                answer += 1
        return answer