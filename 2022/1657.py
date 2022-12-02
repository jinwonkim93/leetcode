from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2): return False
        word1 = sorted(Counter(word1).values())
        word2 = sorted(Counter(word2).values())
        word1 = list(map(str, word1))
        word2 = list(map(str, word2))
        return hash("".join(word1)) == hash("".join(word2))



word1, word2 = "abc", "bca"
word3, word4 = "a", "aa"
word5, word6 = "cabbba", "abbccc"
solution = Solution()
assert solution.closeStrings(word1, word2) == True, "Example 1"
assert solution.closeStrings(word3, word4) == False, "Example 2"
assert solution.closeStrings(word5, word6) == True, "Example 3"