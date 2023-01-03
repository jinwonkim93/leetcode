from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        ans = 0
        for column_string in zip(*strs):
            if "".join(sorted(column_string)) != "".join(column_string): ans += 1
        return ans