import numpy as np
class Solution:
    def MinCost(self,Array,minCostArray,n):
        if(n>=len(Array)):
            return 0
        if(minCostArray[n]!=-1):
            return minCostArray[n]
        minCostArray[n]=min(self.MinCost(Array,minCostArray,n+1),self.MinCost(Array,minCostArray,n+2))+Array[n]
        return minCostArray[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCostArray = np.full(len(cost), -1)
        return min(self.MinCost(cost,minCostArray,0),self.MinCost(cost,minCostArray,1))

        