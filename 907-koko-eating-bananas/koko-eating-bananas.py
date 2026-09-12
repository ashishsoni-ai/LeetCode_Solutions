class Solution:
    def isValid(self,piles,h,mid):
        n = len(piles)
        TotalHour = 0
        for i in range(n):
            TotalHour += piles[i]//mid
            if piles[i] % mid != 0:
                TotalHour += 1
            if TotalHour > h:
                return False
        return True

            
                

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = -1
        low = 1
        high = max(piles)
        while low<=high:
            mid = (low+high)//2
            if self.isValid(piles,h,mid):
                ans = mid
                high = mid -1
            else:
                low = mid + 1

        return ans