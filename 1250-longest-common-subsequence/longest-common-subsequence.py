import numpy as np
class Solution:
    def helper(self,values, text1, text2, n, m):
        if n >= len(text1) or m >= len(text2):
            return 0
        if text1[n] == text2[m]:
            return 1 + self.helper(values,text1, text2, n+1, m+1)
        if values[n][m] != -1:
            return int(values[n][m])

        values[n][m] = max(self.helper(values, text1, text2, n, m+1), self.helper(values, text1, text2, n+1, m))
        return int(values[n][m])
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        values = np.full((len(text1), len(text2)), -1)
        return self.helper(values, text1, text2, 0, 0)

