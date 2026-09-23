class Solution:
    def mergeArrays(self, arr1, arr2):
        i = 0
        j = 0
        k = len(arr1) - 1

        while i <= k and j < len(arr2):

            if arr1[i] < arr2[j]:
                i += 1
                continue

            else:
                temp = arr1[k]
                arr1[k] = arr2[j]
                arr2[j] = temp

                k -= 1
                j += 1

        arr1.sort()
        arr2.sort()
        
        