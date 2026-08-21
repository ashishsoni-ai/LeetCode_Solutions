class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr)<= 1:
            return arr
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        left = self.sortArray(left)
        right = self.sortArray(right)
        return self.merge_sort(left,right)

    def merge_sort(self,left,right):
        i = 0
        j = 0
        m = len(left)
        n = len(right)
        ans = []

        while  i < m and j < n:
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
        if i < m:
            while i < m:
                ans.append(left[i])
                i += 1
        if j < n:
            while j< n:
                ans.append(right[j])
                j += 1
        return ans
        


        