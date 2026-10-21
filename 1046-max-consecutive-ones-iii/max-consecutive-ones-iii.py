class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maxi = 0
        n = len(nums)
        zeroes = 0
        left = 0
        right = 0
        while right < n:
            if nums[right] == 0:
                zeroes += 1
            
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            
            
            maxi = max(maxi,right-left+1)
            right += 1
        return maxi
        