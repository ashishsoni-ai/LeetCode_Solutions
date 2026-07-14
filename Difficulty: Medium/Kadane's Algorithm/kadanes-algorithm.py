class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        n = len(arr)
        curr_sum = 0
        max_sum = arr[0]
        for i in range(n):
            curr_sum += arr[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
                
        return max_sum
            
        