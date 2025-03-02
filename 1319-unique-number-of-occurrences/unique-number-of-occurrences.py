class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # occurence : value
        occurences = {}
        for num in arr:
            if num in occurences:
                occurences[num] += 1
            else:
                occurences[num] = 1
        unique = set()
        for value in occurences:
            unique.add(occurences[value])

        return len(unique) == len(occurences)


