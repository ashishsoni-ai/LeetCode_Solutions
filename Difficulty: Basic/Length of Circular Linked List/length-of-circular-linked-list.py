'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def getLength(self, head):
        # code here
        slow = head
        fast = head
        count = 0
        while True:
            
            slow = slow.next
            fast = fast.next.next
            count += 1
            if slow == fast:
                return count

            
        