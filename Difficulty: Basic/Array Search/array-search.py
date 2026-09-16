class Solution:
    def find(self,arr,x,i):

        if i >= len(arr) :
            return -1
        if arr[i] == x:
            return i
        
        return self.find(arr,x,i+1)
        
    def search(self, arr, x):

        return self.find(arr,x,0)