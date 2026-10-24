class Solution:
    def solve(self, index, arr, k, total):
        if total == k:
            return True

        if index >= len(arr) or total > k:
            return False

        # Include
        if self.solve(index + 1, arr, k, total + arr[index]):
            return True

        # Exclude
        if self.solve(index + 1, arr, k, total):
            return True

        return False

    def checkSubsequenceSum(self, arr, k):
        return self.solve(0, arr, k, 0)