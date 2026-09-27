class Solution:
    def solve(self,candidates,target,index,current,ans):
        if index >= len(candidates) or target < 0:
            return
        if target == 0:
            ans.append(current.copy())
            return 
        #include
        current.append(candidates[index])
        self.solve(candidates, target-candidates[index], index, current, ans)

        current.pop()

        #exclude
        self.solve(candidates, target, index+1, current, ans)

        
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        current = []
        index = 0
        self.solve(candidates, target, index, current, ans)

        return ans