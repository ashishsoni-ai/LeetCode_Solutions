'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteHead(self, head):
        # code here
        curr = head
        curr = curr.next
        head = curr
        return head
    