class Solution:

    def isValidAns(self, arr, k, mid):
        n = len(arr)

        cowCount = 1
        lastPosition = 0

        for i in range(1, n):

            if arr[i] - arr[lastPosition] >= mid:
                cowCount += 1
                lastPosition = i

            if cowCount == k:
                return True

        return False

    def aggressiveCows(self, arr, k):
        arr.sort()

        n = len(arr)

        left = 0
        right = arr[n - 1] - arr[0]

        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if self.isValidAns(arr, k, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans