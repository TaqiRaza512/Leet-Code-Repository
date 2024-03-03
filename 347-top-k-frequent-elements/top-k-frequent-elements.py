class Solution(object):
    def topKFrequent(self, nums, k):
        HashMap={}
        res=[]
        freq=[[] for i in range(len(nums)+1)]
        for i in nums:
            HashMap[i]=1+HashMap.get(i,0)
        
        for n,c in HashMap.items():
            freq[c].append(n)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if(len(res)==k):
                    return res