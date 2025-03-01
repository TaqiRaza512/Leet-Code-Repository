class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k - 1

        average = sum(nums[:k])/k
        max_average = average

        while (right < len(nums)-1):
            right += 1
            average = average - nums[left]/k + nums[right]/k
            max_average = max(average, max_average)
            left += 1
        return max_average


        