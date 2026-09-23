class Solution:
    def fourSum(self, arr, target):
        ans = []
        arr.sort()
        n = len(arr)
        for i in range(n):
            if i>0 and arr[i] == arr[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and arr[j] == arr[j-1]:
                    continue
                left = j+1
                right = n-1
                while left<right :
                    total = arr[i] +arr[j] +arr[left] + arr[right]
                    if total == target:
                        ans.append([arr[i], arr[j], arr[left], arr[right]])
                        left += 1
                        right -= 1
                        while left < right and arr[left-1] == arr[left]:
                            left += 1
                        while left < right and arr[right] == arr[right+1]:
                            right -= 1
   
                    elif total>target:
                        right -= 1
                    else:
                        left += 1
        return ans
        
        