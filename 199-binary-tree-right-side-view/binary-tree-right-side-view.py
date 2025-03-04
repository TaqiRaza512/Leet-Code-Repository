# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        prev_q = []
        queue = [root]
        result = []

        while(len(queue) != 0):
            result.append(queue[-1].val)
            prev_q = queue
            queue = []
            for node in prev_q:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result