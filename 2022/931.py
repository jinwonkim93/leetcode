from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for r in range(1, len(matrix)):
            for c in range(len(matrix[0])):
                c_min = c - 1 if c > 0 else 0
                c_max = c + 2
                matrix[r][c] += min(matrix[r - 1][c_min:c_max])
        return min(matrix[-1])