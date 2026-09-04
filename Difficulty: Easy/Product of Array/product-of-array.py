class Solution:
    def product(self, arr):
        # code here
        ans = 1
        for num in arr:
            ans *= num
        if ans < 1000000007:
            return ans
        else:
            return ans%1000000007
        
        