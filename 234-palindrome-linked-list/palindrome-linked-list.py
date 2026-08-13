class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        temp = head

        # Put all values into stack
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next

        # Compare linked list with stack
        temp = head
        while temp is not None:
            if temp.val != stack[-1]:
                return False

            temp = temp.next
            stack.pop()

        return True