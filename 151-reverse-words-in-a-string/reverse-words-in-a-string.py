class Solution:
    def reverseWords(self, s: str) -> str:
        trim_string = s.split()
        res = ''
        space = " "

        for s in trim_string:
            if res == "":
                space = ""
            else: 
                space = " "    
            res = s + space + res
        return res


        