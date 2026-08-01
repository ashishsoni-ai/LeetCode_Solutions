class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            if arr[mid] < arr[mid-1]:
                r = mid-1
            else:
                l = mid+1
        return 1


        