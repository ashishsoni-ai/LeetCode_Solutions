class Solution:

    def solve(self, candidates, target, index, current, ans,count,k):



        if target == 0 and count == k:
            ans.append(current.copy())
            return

        if index >= len(candidates) or target < 0:
            return

        # Include
        current.append(candidates[index])

        self.solve(candidates,target - candidates[index],index + 1,current,ans,count+1,k)

        current.pop()

        # Exclude
        index += 1

        while index < len(candidates) and candidates[index] == candidates[index - 1]:
            index += 1

        self.solve(candidates,target,index,current,ans,count,k)

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        candidates = [1,2,3,4,5,6,7,8,9]
        count = 0
        target = n
        ans = []
        current = []
        index = 0

        self.solve(candidates, target, index, current, ans,count , k)

        return ans
        