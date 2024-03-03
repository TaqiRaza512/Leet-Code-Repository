class Solution(object):
    def isAnagram(self, s, t):
        countS={}
        countT={}
        if(len(s)!=len(t)):
            return False
        for val in s:
            countS[val]=1+countS.get(val,0)
        for val in t:
            countT[val]=1+countT.get(val,0)
        print(countT)
        for i in countT:
            if(countT[i]!=countS.get(i,0)):
                return False
        return True
