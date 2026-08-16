class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or head.next is None or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Remove unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Make list circular
        tail.next = head

        # Find new tail
        steps = length - k
        newTail = head

        for i in range(1, steps):
            newTail = newTail.next

        # New head
        newHead = newTail.next

        # Break the circle
        newTail.next = None

        return newHead