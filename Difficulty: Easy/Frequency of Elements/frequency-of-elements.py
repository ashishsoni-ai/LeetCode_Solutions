class Solution:
    def countFreq(self, arr):
        #code here
        freq = {}
        n = len(arr)
        for i in range(n):
            freq[arr[i]] = freq.get(arr[i],0)+1
        ans = []
        for key,value in freq.items():
            ans.append([key,value])
        return ans
        