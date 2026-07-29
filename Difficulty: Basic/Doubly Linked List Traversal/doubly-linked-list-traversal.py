''' Structure of doubly linked list Node
  class Node:
      def __init__(self, x):
          self.data = x
          self.next = None
          self.prev = None
'''
class Solution:
    def displayList(self, head):
        forward = []
        backward = []

        current = head

        # Forward traversal
        while current:
            forward.append(current.data)

            if current.next is None:
                last = current

            current = current.next

        # Backward traversal
        current = last

        while current:
            backward.append(current.data)
            current = current.prev

        return forward, backward
            
        