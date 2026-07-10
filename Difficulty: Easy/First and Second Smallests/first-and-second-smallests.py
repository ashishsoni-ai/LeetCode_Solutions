class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        arr.sort()
        mini = arr[0]
        mini2 = None
        
        for num in arr:
            if num != mini:
                mini2 = num
                break
                
        if mini2 is None:
            return [-1]
        return [mini,mini2]
