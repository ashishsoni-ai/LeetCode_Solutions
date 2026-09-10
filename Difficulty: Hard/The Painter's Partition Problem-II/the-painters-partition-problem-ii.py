class Solution:
    def IsValidAnswer(self, arr, k, mid):
        CountPainter = 1
        TotalTime = 0

        for i in range(len(arr)):
            if TotalTime + arr[i] <= mid:
                TotalTime += arr[i]
            else:
                CountPainter += 1

                if CountPainter > k or arr[i] > mid:
                    return False

                TotalTime = arr[i]

        return True
            

        
    def minTime (self, arr, k):

        n = len(arr)
        low = max(arr)
        high = sum(arr)
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if self.IsValidAnswer(arr, k , mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

                
        return ans