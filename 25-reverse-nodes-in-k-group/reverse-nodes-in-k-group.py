# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        temp = head
        count = 0
        while temp != None and count<k:
            temp = temp.next
            count += 1
        if count < k:
            return head
        if head is None:
            return None
        curr = head
        prev = None
        forward = None
        count = 0
        while curr != None and count < k:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
            count += 1

        if forward is not None:
            head.next = self.reverseKGroup(forward,k)
        return prev
        
        