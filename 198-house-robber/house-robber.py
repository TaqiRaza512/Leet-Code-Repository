import numpy as np
class Solution:
    def MaxRob(self,nums,MaxRobCount,n):
        if(n>=len(nums)):
            return 0
        if(MaxRobCount[n]!=-1):
            return MaxRobCount[n]
        MaxRobCount[n]=nums[n]+max(self.MaxRob(nums,MaxRobCount,n+2),self.MaxRob(nums,MaxRobCount,n+3),self.MaxRob(nums,MaxRobCount,n+4))
        return MaxRobCount[n]
    def rob(self, nums: List[int]) -> int:
        MaxRobCount=np.full(len(nums),-1)
        self.MaxRob(nums,MaxRobCount,0)
        if(len(nums)>=2):
            return max(self.MaxRob(nums,MaxRobCount,0),self.MaxRob(nums,MaxRobCount,1))
        return MaxRobCount[0]