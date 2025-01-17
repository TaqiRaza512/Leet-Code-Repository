# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         count = 1
#         discarded = 0
#         prev_value = nums[0]
#         i = 1
#         while (i < len(nums) - discarded):
#             if nums[i] == prev_value:
#                 count += 1
#             else:
#                 count = 1

#             prev_value = nums[i]
        
#             if count > 2:
#                 discarded += 1
                
#                 for c in range(i,len(nums)-1):
#                     nums[c] = nums[c+1]
#                 i -= 1
#             i += 1
#         return len(nums) - discarded


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1 

        return k