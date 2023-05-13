from functools import lru_cache

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        
        @lru_cache()
        def dp(step, zero, one):
            if step == 0: return 1
            cnt = 0
            if step >= zero:
                cnt += dp(step - zero, zero, one)
            if step >= one:
                cnt += dp(step - one, zero, one)
            
            return cnt % mod
        
        
        
        return sum([dp(step, zero, one) for step in range(low, high+1)]) % mod