# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_list(self, head):
        if not head.next:
            return head
        prev = head
        current = head.next
        next_node = head.next.next
        prev.next = None
        while(True):
            current.next = prev
            prev = current
            current = next_node
            if (next_node):
                next_node = next_node.next
            else:
                break
        return prev

    def length(self, head):
        size = 0
        while(head):
            size += 1
            head = head.next
        return size
    def next_half_list(self, head, size):
        i = 0
        while(i < size/2 ):
            i += 1
            head = head.next
        return head
    def pairSum(self, head: Optional[ListNode]) -> int:
        size = self.length(head)
        next_mid = self.reverse_list(self.next_half_list(head, size))
        max_sum = 0

        while(next_mid):
            max_sum = max(int(next_mid.val) + int(head.val), max_sum)
            next_mid = next_mid.next
            head = head.next
        return max_sum
