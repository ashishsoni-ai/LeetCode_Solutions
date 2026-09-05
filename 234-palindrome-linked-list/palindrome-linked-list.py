class Solution:
    def findmid(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head is None or head.next is None:
            return True

        # Find middle
        mid = self.findmid(head)

        # Reverse second half
        second_half = self.reverse(mid)

        # Compare both halves
        first = head
        second = second_half

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True