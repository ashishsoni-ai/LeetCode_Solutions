class Solution:
    def missingNum(self, arr):
        # code here
        
        n = len(arr)+1
        add = 0
        #total sum
        for i in range(0,n-1):
            
            add += arr[i]
        #expected sum
        fullsum = n*(n+1)//2
        
        return fullsum-add
            