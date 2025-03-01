class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """

        zero =  0
        number = 0

        while(zero < len(nums) and number < len(nums)):

            if nums[zero] == 0 and nums[number] != 0:
                if zero < number:
                    nums[zero], nums[number] = nums[number], nums[zero]
                else:
                    number += 1

            if nums[zero] != 0:
                zero += 1
            if nums[number] == 0:
                number += 1
            


        
        