class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq = {}
        ans = [0,0]
        for i in range(len(grid)):
            for j in range(len(grid)):
                num = grid[i][j]

                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1

        for i in range(1, len(grid) * len(grid) + 1):
            if i in freq:
                if freq[i] == 2:
                    ans[0] = i
            else:
                ans[1] = i
        return ans

        