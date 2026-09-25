class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        ans = float("-inf")
        prefix = 1
        suffix = 1
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix = prefix * nums[i]
            suffix = suffix * nums[n-i-1]

            ans = max(ans,max(prefix,suffix))
        return ans
        