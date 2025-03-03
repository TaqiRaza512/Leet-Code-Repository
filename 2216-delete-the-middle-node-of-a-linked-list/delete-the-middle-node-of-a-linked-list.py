# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head or not head.next):
            return None

        double_jump = head
        single_jump = head
        prev_jump = None

        while(double_jump and double_jump.next):
            
            double_jump = double_jump.next.next
            prev_pointer = single_jump
            single_jump = single_jump.next

        prev_pointer.next = single_jump.next

        return head