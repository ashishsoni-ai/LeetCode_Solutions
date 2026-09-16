class Solution:
    def binarysearch(self,nums,target,low,high):
        if low>high:
            return -1
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid+1
        else:
            high = mid-1

        return self.binarysearch(nums,target,low,high)
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        return self.binarysearch(nums,target,low,high)

        