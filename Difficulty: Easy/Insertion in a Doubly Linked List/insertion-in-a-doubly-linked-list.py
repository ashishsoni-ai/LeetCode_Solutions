class Solution:
    def insertAtPos(self, head, p, x):
        newNode = Node(x)

        # Empty list
        if head is None:
            return newNode

        current = head
        count = 0

        # Move to the p-th node
        while current.next and count < p:
            current = current.next
            count += 1

        # Insert after current
        newNode.next = current.next
        newNode.prev = current

        if current.next:
            current.next.prev = newNode

        current.next = newNode

        return head