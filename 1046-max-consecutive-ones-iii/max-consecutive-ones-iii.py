class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        zeros_encountered = 0
        max_string = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_encountered += 1
            
            while (zeros_encountered > k):
                if nums[left] == 0:
                    zeros_encountered -= 1
                left += 1

            max_string = max(right - left + 1, max_string)
        return max_string


