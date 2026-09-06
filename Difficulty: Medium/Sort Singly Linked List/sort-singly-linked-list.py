''' Structure of a Linked List Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def mergeTwoSortedLinkedLists(self,left,right):
        dummy = Node(-1)
        temp = dummy
        while left and right:
            if left.data<=right.data:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
            
        if left is not None:
            temp.next = left
        else:
            temp.next = right
            
        return dummy.next
            
            
        
    
    def divide(self,head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        right = slow.next
        slow.next = None
        
        left = self.divide(head)
        right = self.divide(right)
        
        return self.mergeTwoSortedLinkedLists(left,right)
            
    def sortLL(self, head):
        #code here
        return self.divide(head)
        