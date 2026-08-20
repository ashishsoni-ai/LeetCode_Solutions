'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def modularNode(self, head, k):
        # code Here
        curr = head
        ans = -1
        count = 0
        while curr is not None:
            count += 1
            if count % k == 0:
                ans = curr.data
            curr = curr.next
        return ans
        