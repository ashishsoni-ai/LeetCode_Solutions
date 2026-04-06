class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        ans = -1 
        for i in range(len(capacity)):
            if capacity[i] >= itemSize :
                if ans == -1 or capacity[ans]>capacity[i]:
                    ans = i
        return ans

        

        