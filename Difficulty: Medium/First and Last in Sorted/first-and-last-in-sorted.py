class Solution:
    def find(self, arr, x):
        # code here
        n = len(arr)
        first = -1
        last = -1
        for i in range(n):
            if arr[i] == x:
                if first == -1:
                    
                    first = i
                last = i

        return [first,last]
        