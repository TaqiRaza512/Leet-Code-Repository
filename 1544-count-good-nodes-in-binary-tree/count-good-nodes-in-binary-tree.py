# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def counting_goods(self, root, current_max):
        count = 0
        if not root:
            return 0
        if current_max <= root.val:
            count += 1
            current_max = root.val
            

        return self.counting_goods(root.left, current_max) + self.counting_goods(root.right, current_max) + count

    def goodNodes(self, root: TreeNode) -> int:
        current_max = root.val

        return self.counting_goods(root, current_max)