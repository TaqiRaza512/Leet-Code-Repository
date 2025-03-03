# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        even = head
        odd_temp = head.next
        odd = head.next
        temp = odd.next


        while temp and odd and even:
            temp = odd.next
            even.next = temp
            if temp:
                odd.next = temp.next
            if even.next:
                even = even.next
            odd = odd.next

        even.next = odd_temp

        return head


        return even
        