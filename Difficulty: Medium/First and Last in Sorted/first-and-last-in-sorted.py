class Solution:
    def first(self, arr, x):
        n = len(arr)
        ans = -1
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        if ans == -1 or arr[ans] != x:
            return -1
        return ans

    def last(self, arr, x):
        n = len(arr)
        ans = n
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def find(self, arr, x):
        first = self.first(arr, x)

        if first == -1:
            return [-1, -1]

        last = self.last(arr, x)

        return [first, last - 1]