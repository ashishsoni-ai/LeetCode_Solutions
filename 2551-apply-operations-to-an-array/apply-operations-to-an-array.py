class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        current = 0
        for i in range (len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = 2*nums[i]
                nums[i+1] = 0
        for i in range(len(nums)):
            
            if nums[i] != 0:
                nums[current],nums[i] = nums[i],nums[current]
                current +=1
        return nums
        