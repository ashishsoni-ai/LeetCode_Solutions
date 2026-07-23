class Solution:
    def floorSqrt(self, n): 
        # code here
        if n < 2:
            return n
        ans = 0
        l = 0
        r = n
        while l<=r:
            mid = (l+r)//2
            if mid*mid == n:
                return mid
                
            elif mid*mid < n:
                ans = mid
                l = mid+1
                
            else:
                r = mid - 1
        return ans