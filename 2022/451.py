from collections import Counter



class Solution:
    def frequencySort(self, s: str) -> str:
        s_count = Counter(s)
        ans = ""
        for key, value in s_count.most_common():
            ans += key*value
        return ans


s1 = "tree"
s2 = "cccaaa"
s3 = "Aabb"
solution = Solution()
assert solution.frequencySort(s1) == "eetr", "Example1"
assert solution.frequencySort(s2) == "cccaaa", "Example2"
assert solution.frequencySort(s3) == "bbAa", "Example3"