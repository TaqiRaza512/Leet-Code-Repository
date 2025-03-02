class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        post_sum = sum(nums[1:])
        index = 0
        pre_sum = 0
        if len(nums)<=1:
            return 0
        if pre_sum == post_sum:
            return index
                
        while (index < len(nums)-1):
            
            pre_sum += nums[index]
            index += 1
            post_sum -= nums[index]
            if pre_sum == post_sum:
                return index

            
        return -1

        

        