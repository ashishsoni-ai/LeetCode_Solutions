# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        ans = []
        while temp is not None:
            ans.append(temp.val)
            temp = temp.next
        ans.sort()
        temp = head
        for value in ans:
            temp.val = value
            temp = temp.next

        return head



        