class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        n = len(arr)
        ans = False
        arr.sort()
        
        for i in range(n):
            if i != 0 and arr[i] == arr[i-1]:
                continue
            left = i+1
            right = n-1
            
            while left<right:
                if arr[i] + arr[left] + arr[right] == target:
                    ans = True
                    return ans
                elif arr[i] + arr[left] + arr[right] > target:
                    right -= 1
                else:
                    left += 1
        return ans
        
        
            