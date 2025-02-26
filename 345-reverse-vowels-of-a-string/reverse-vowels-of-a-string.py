class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        vowels = 'aeiou'

        while (left < right):
            if s[left].lower() in vowels:
                if s[right].lower() in vowels:
                    s[left], s[right] = s[right], s[left]
                    right = right - 1
                    left = left + 1
                else:
                    right = right - 1
            else:
                left = left + 1
        return "".join(s)