class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        result = []
        dq = []

        for i in range(n):
            # Step 1: Remove indices outside the window
            while dq and dq[0] <= i-k:
                dq.pop(0)
            # Step 2: Remove smaller elements from the back
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            # Step 3: Push current index
            dq.append(i)
            # Step 4: Store maximum
            if i >= k-1:
                result.append(nums[dq[0]])
        return result

        