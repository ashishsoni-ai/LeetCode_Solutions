class Solution:
    def Find(self,arr,i,max_element):
        length = len(arr)
        if i >= length:
            return max_element
         
        if arr[i] > max_element:
            max_element = arr[i]
          
        return self.Find(arr,i+1,max_element)

    def largest(self, arr):
        return self.Find(arr,0,float("-inf"))
        
        
