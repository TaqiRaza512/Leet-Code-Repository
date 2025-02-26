class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        print(s)
        left = 0
        right = len(s) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        while (left < right):
            if s[left].lower() in vowels:
                if s[right].lower() in vowels:

                    temp = s[left]
                    s[left] = s[right]
                    s[right] = temp
                    right = right - 1
                    left = left + 1
                else:
                    right = right - 1
            else:
                left = left + 1
                    

        return "".join(s)