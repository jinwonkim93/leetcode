from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        max_money = [0] * n

        for i in range(n):
            if i < 2:
                if i == 0:
                    max_money[i] = nums[i]
                if i == 1:
                    max_money[i] = max(max_money[i-1], nums[i])
            else:
                max_money[i] = max(max_money[i-2] + nums[i], max_money[i-1])
        
        return max_money[n-1]