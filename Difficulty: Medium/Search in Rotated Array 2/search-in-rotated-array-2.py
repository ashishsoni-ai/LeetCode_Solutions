class Solution:
    def search(self, arr, key):
        # code here
        n = len(arr)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] == key:
                return True
            if arr[low] == arr[mid] and arr[high]==arr[mid]:
                low = low+1
                high = high -1
                continue
            if arr[low]<=arr[mid]:
                if arr[low]<= key < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            else:
                if arr[mid] <= key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return False
                    
                
