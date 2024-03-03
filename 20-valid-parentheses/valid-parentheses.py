class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            if(i=="(" or i=="[" or i=="{"):
                stack.append(i)
                continue
            if(len(stack)>0):
                if(i==')'):
                    if(stack.pop()!="("):
                        return False
                elif(i==']'):
                    if(stack.pop()!="["):
                        return False
                elif(i=='}'):
                    if(stack.pop()!="{"):
                        return False
            else:
                return False
        if(len(stack)==0):
            return True
            