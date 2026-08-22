class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for num in nums:
            if num == target:
                return True
        return False 
            
        