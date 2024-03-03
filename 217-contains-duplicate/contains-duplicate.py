class Solution(object):

    def containsDuplicate(self, nums):
        UniqueValues=set()
        for val in nums:
            if val in UniqueValues:
                return True
            UniqueValues.add(val)
        return False
