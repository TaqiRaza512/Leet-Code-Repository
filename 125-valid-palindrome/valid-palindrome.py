class Solution(object):
    def isAlphaNumeric(self,value):
        if((ord(value)<=122 and ord(value)>=97) or (ord(value)<=90 and ord(value)>=65) or (ord(value)<=57 and ord(value)>=48)):
            return True
        return False
    def isPalindrome(self, s):
        left=0
        right=len(s)-1
        if(left==right and left<len(s) and right>=0):
            return True
        while(left<right):
            while not (self.isAlphaNumeric(s[left])) and left<right:
                left+=1
            while not (self.isAlphaNumeric(s[right]))and right>left:
                right-=1
            
            if not (lower(s[left])==lower(s[right])):
                return False
            left+=1
            right-=1

        return True