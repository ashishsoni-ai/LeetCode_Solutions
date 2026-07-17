class Solution:
    def maxConsecBits(self, arr):
        #code here 
        count = 1
        maximum = 1
        n = len(arr)
        for i in range(1,n):
            if arr[i] == arr[i-1]:
                count += 1
                maximum = max(maximum,count)
            else:
                count = 1
        return maximum
                
        