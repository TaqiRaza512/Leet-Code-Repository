class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = set()
        result = []
        for i in nums1:
            if i not in nums2:
                answer.add(i)

        result.append(list(answer))
        answer = set()

        for i in nums2:
            if i not in nums1:
                answer.add(i)
        result.append(list(answer))

        return result