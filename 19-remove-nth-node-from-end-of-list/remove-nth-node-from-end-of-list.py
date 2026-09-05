# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length = 0
        # curr = head
        # while curr is not None:
        #     length += 1
        #     curr = curr.next
        # if length == n:        
        #     return head.next

        # position_to_stop = length-n
        # count = 1
        # temp = head
        # while count<position_to_stop:
        #     count += 1
        #     temp = temp.next
        # temp.next = temp.next.next

        # return head

        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

        






        