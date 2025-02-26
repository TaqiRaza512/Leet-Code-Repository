class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        pre_mult = 1
        post_mult = 1


        for i in range(len(nums) - 1):
            pre_mult = pre_mult * nums[i]
            result[i+1] = pre_mult

        for i in range(len(nums) - 2, -1, -1):
            post_mult = post_mult * nums[i+1]
            result[i] = result[i] * post_mult

        return result
            
