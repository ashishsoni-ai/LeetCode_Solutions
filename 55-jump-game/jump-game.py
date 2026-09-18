#Recursion Solution


# class Solution:

#     def solve(self, index, nums):

#         # Last index reached
#         if index == len(nums) - 1:
#             return True

#         # Index array ke bahar chala gaya
#         if index >= len(nums):
#             return False

#         # Current value 0 hai, aage nahi ja sakte
#         if nums[index] == 0:
#             return False

#         JumpValue = nums[index]

#         OverallAns = False

#         for i in range(1, JumpValue + 1):

#             recAns = self.solve(index + i, nums)

#             OverallAns = OverallAns or recAns

#         return OverallAns

#     def canJump(self, nums: list[int]) -> bool:
#         return self.solve(0, nums)

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxi = 0
        for i in range(len(nums)):
            if i > maxi:
                return False
            maxi = max(maxi,i+nums[i])
        return True
        