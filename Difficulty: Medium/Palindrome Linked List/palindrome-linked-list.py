'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def findmid(self,head):
        slow = head
        fast = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self,head):
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev 
            prev = curr
            curr = next_node
        return prev
            

    def isPalindrome(self, head):
        # code here
        if head is None or head.next is None:
            return True
        
        mid = self.findmid(head)
        second_half = self.reverse(mid)
        
        first = head
        second = second_half
        
        while second is not None:
            if first.data != second.data:
                return False
            first = first.next
            second = second.next
        return True
        
        