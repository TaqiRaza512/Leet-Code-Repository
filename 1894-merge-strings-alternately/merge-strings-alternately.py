class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_array = []
        
        for a,b in zip(word1, word2):
            merged_array.append(a+b)

        merged_array.append(word1[len(word2):])
        merged_array.append(word2[len(word1):])
        return "".join(merged_array)
        
        