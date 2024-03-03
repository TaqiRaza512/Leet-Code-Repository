class Solution(object):
    def twoSum(self, nums, target):
        HashMap={}
        for i,n in enumerate(nums):
            diff =target-n

            if diff in HashMap:
                return [HashMap[diff],i]
            HashMap[n]=i
        