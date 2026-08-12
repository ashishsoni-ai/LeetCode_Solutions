class Solution:
    def maxLength(self, arr):
        # code here
        ans = 0
        hashmap = {0:-1}
        sum1 = 0
        
        for i in range(len(arr)):
            sum1 += arr[i]
            if sum1 in hashmap:
                ans = max(ans, i - hashmap[sum1])
            else:
                hashmap[sum1] = i
        return ans
                