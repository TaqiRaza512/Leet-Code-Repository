# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path_sum_checking(self, root, current_sum, targetSum):
        if not root:
            return 0
        count = 0
        if current_sum == targetSum:
            count += 1
        if root.right:
            count += self.path_sum_checking(root.right, current_sum + root.right.val, targetSum)
            #  + self.path_sum_checking(root.right, root.right.val, targetSum) 
        if root.left:
            count += self.path_sum_checking(root.left, current_sum + root.left.val, targetSum) 
            # + self.path_sum_checking(root.left, root.left.val, targetSum)
        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.path_sum_checking(root, root.val,targetSum)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)