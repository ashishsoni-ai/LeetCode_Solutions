class Solution:
    def majorityElement(self, arr):
        #code here
        count = 0
        element = None
        for num in arr:
            if count == 0:
                count = 1
                element = num
            elif num == element:
                count += 1
            else:
                count -= 1
        count = 0
        for num in arr:
            if num == element :
                count +=1
            if count > len(arr)//2:
                return element
        return -1