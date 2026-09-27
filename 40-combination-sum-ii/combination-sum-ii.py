class Solution:

    def solve(self, candidates, target, index, current, ans):

        if target == 0:
            ans.append(current.copy())
            return

        if index >= len(candidates) or target < 0:
            return

        # Include
        current.append(candidates[index])

        self.solve(
            candidates,
            target - candidates[index],
            index + 1,
            current,
            ans
        )

        current.pop()

        # Exclude
        index += 1

        while index < len(candidates) and candidates[index] == candidates[index - 1]:
            index += 1

        self.solve(
            candidates,
            target,
            index,
            current,
            ans
        )

    def combinationSum2(self, candidates, target):
        candidates.sort()

        ans = []
        current = []

        self.solve(candidates, target, 0, current, ans)

        return ans