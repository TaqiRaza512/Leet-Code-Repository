import numpy as np
class Solution:
    # Memoization Technique
    def CountingStairs(self,n,array):
        if(n==0):
            return 1
        elif(n<0):
            return 0
        elif(array[n-1]!=0):
            return array[n-1]
        array[n-1]=self.CountingStairs(n-1,array)+self.CountingStairs(n-2,array)
        return array[n-1]
    def climbStairs(self, n: int) -> int:
        if(n<0):
            return 0
        array=np.zeros(n)
        array=self.CountingStairs(n,array)
        return int(array)


        