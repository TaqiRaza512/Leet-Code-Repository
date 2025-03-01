class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        small_pointer = 0
        large_pointer = 0
        
        while large_pointer < len(t) and small_pointer < len(s):
            if s[small_pointer] == t[large_pointer]:
                small_pointer += 1
            large_pointer += 1

        return small_pointer == len(s)
        