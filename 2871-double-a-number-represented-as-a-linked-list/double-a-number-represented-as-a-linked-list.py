# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        curr = head
        prev = None
        while curr!=None:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
        return prev



    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        temp = head
        carry = 0
        while temp != None:
            NodeValue = 2*(temp.val) + carry
            temp.val = NodeValue % 10
            carry = NodeValue // 10
            
            if temp.next == None and carry != 0:
                temp.next = ListNode(carry)
                break
            temp = temp.next
        head = self.reverse(head)
        return head

        