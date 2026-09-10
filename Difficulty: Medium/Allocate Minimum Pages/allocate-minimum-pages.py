class Solution:
    def isValidAnswer(self,arr,k,mid):
        
        n = len(arr)
        StudentCount = 1
        pages = 0
        for i in range(n):
            if pages + arr[i] <= mid:
                pages += arr[i]
            else:
                StudentCount += 1
                if StudentCount > k or arr[i] > mid:
                    return False
                pages = 0
                pages += arr[i]
                
        return True       
            
        
    def findPages(self, arr, k):
        
        # code here
        n = len(arr)
        if n < k:
            return -1
        start = max(arr)
        end = sum(arr)
        ans = -1
        while start<=end:
            mid = (start+end)//2
            if self.isValidAnswer(arr, k, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
                
        return ans
