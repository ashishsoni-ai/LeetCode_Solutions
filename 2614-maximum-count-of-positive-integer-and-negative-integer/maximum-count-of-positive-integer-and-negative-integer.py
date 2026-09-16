class Solution:
    def positive(self,nums):
        n= len(nums)
        low = 0
        high = n-1
        ans = n
        while low <= high:
            mid = (low+high)//2
            if nums[mid]> 0:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return n-ans
    
    def negative(self,nums):
        n= len(nums)
        low = 0
        high = n-1
        ans = n
        while low <= high:
            mid = (low+high)//2
            if nums[mid]>= 0:
                ans = mid
                high = mid - 1
                
            else:
                low = mid + 1

        return ans

    def maximumCount(self, nums: List[int]) -> int:
        pos = self.positive(nums)
        neg = self.negative(nums)
        return max(pos,neg)

        