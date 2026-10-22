
class Solution:
    def solve(self, nums, index, subset, result):
        if index >= len(nums):
            result.append(subset.copy())
            return

        # Include current element
        subset.append(nums[index])
        self.solve(nums, index + 1, subset, result)

        # Backtrack
        subset.pop()

        # Exclude current element
        self.solve(nums, index + 1, subset, result)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []
        self.solve(nums, 0, subset, result)
        return result
