class Solution:
    def longestConsecutive(self, arr):
        # code here
        arr.sort()
        count = 1
        max_seq = 0
        for i in range(len(arr)):
            if arr[i] == arr[i-1]:
                continue
            if arr[i] == arr[i-1]+1:
                count += 1
                
            else:
                count = 1
            max_seq = max(max_seq,count)
        return max_seq
                
            