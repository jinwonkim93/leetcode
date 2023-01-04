from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans = 0
        for not_complete in Counter(tasks).values():
            if not_complete == 1: return -1
            if not_complete%3 != 0: ans += 1
            ans += not_complete//3
        return ans