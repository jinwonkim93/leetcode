class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        cur = 1
        for _ in range(1, n+1):
            temp = cur
            cur = cur + prev
            prev = temp

        return cur