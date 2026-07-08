class Solution:
    def removeDuplicates(self, arr):
        # code here
        n = len(arr)
        if n == 0:
            return []
        i =  0
        nums = []
        nums.append(arr[0])
        for j in range(1,n):
            if arr[i] != arr[j]:
                nums.append(arr[j])
                i = j
        return nums
        

        
            
                