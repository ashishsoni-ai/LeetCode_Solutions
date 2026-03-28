class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr1 = []
        arr2 = []
        for i in range (len(nums)):
            if nums[i] == 0:
                arr1.append(0)
            else:
                arr2.append(nums[i])
        nums[:] = arr2 +arr1