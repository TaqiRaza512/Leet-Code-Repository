class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sub_string = s[:k]
        max_vowels = 0
        vowels = 0
        total_vowels = "aeiou"
        left = 0
        right = k

        for i in sub_string:
            if i.lower() in total_vowels:
                vowels += 1
        max_vowels = max(vowels, max_vowels)
        while(right < len(s)):
            if k == max_vowels:
                return max_vowels


            if s[left].lower() in total_vowels:
                vowels -= 1

            if s[right].lower() in total_vowels:
                vowels += 1

            left += 1
            right += 1
            max_vowels = max(vowels, max_vowels)
        
        return max_vowels