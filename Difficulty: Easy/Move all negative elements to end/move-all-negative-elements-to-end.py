class Solution:
    def segregateElements(self, arr):
        positive = []
        negative = []
    
        for x in arr:
            if x >= 0:
                positive.append(x)
            else:
                negative.append(x)
    
        result = positive + negative
        
        for i in range(len(arr)):
            arr[i] = result[i]
        return arr