class Solution(object):
    def maxProfit(self, prices):
        max_Profit=0
        l=0
        r=1
        while(l<r and r<len(prices)):
            profit=prices[r]-prices[l]
            max_Profit=max(profit,max_Profit)
            if(profit<0):
                l=r
            r+=1
        return max_Profit

        