import math
from typing import List

class Solution:
    def backtrack(self, nums, mask: int, pairs_picked: int, memo: List[int]) -> int:
        if 2 * pairs_picked == len(nums):
            return 0
        
        if memo[mask] != -1:
            return memo[mask]
        
        max_score = 0

        for first_index in range(len(nums)):
            for second_index in range(first_index + 1, len(nums)):

                if (mask >> first_index) & 1 == 1 or (mask >> second_index) & 1 == 1:
                    continue

                new_mask = mask | (1 << first_index) | (1 << second_index)

                cur_score = (pairs_picked + 1) * math.gcd(nums[first_index], nums[second_index])
                remaining_score = self.backtrack(nums, new_mask, pairs_picked + 1, memo)

                max_score = max(max_score, cur_score + remaining_score)
        memo[mask] = max_score
        return max_score
    
    def maxScore(self, nums: List[int]) -> int:
        memo_size = 1 << len(nums)
        memo = [-1] * memo_size
        return self.backtrack(nums, 0, 0, memo)