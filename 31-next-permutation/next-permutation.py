class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        gola_inx  = -1
        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                gola_inx = i-1
                break
        
        # If gola exists
        SwapElement = gola_inx
        if gola_inx != -1:
            for j in range(n-1,0,-1):
                if nums[j] > nums[gola_inx]:
                    SwapElement = j
                    break
            nums[gola_inx],nums[SwapElement] = nums[SwapElement],nums[gola_inx]
        # Reverse remaining part
        start = gola_inx+1
        end = n-1
        while start<end:
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1

        