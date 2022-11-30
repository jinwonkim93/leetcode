from collections import defaultdict
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur_dict = defaultdict(int)

        for num in arr:
            if num not in occur_dict.keys():
                occur_dict[num] = 1
            else:
                occur_dict[num] += 1
        print(occur_dict.values())
        print(set(occur_dict.values()))
        return len(occur_dict.values()) == len(set(occur_dict.values()))

arr = [1,2,2,1,1,3]
solution = Solution()
print(solution.uniqueOccurrences(arr))

#use counter next time