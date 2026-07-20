class Solution:
    def findFloor(self, arr, x):
        # code here
        low = 0
        n = len(arr)
        ans = -1
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid] <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid-1
        return ans