class Solution:
    def findExtra(self, a, b):
        low = 0
        high = len(b) - 1

        while low <= high:
            mid = (low + high) // 2

            if a[mid] == b[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return low