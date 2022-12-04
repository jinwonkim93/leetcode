from typing import List
import math
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        min_avg_diff = math.inf

        prefix_sum = [0] * (n + 1)
        suffix_sum = [0] * (n + 1)

        for idx in range(n):
            prefix_sum[idx + 1] = prefix_sum[idx] + nums[idx]
        
        for idx in range(n - 1, -1, -1):
            suffix_sum[idx] = suffix_sum[idx + 1] + nums[idx]
        
        for idx in range(n):
            left_part_average = prefix_sum[idx + 1]
            left_part_average //= (idx + 1)
            right_part_average = suffix_sum[idx + 1]
            if idx != n-1:
                 right_part_average //= (n - idx - 1) 
            cur_diff = abs(left_part_average - right_part_average)
            if cur_diff < min_avg_diff:
                min_avg_diff = cur_diff
                ans = idx
        return ans


nums1 = [2,5,3,9,5,3]
nums2 = [0]
nums3 = [0,0,0,0,0]
nums4 = [4,2,0]
nums5 = [1,2,3,4,5]
solution = Solution()
assert solution.minimumAverageDifference(nums1) == 3, "Example1"
print()
assert solution.minimumAverageDifference(nums2) == 0, "Example2"
print()
assert solution.minimumAverageDifference(nums3) == 0, "Example3"
print()
assert solution.minimumAverageDifference(nums4) == 2, "Example4"
print()
assert solution.minimumAverageDifference(nums5) == 0, "Example5"