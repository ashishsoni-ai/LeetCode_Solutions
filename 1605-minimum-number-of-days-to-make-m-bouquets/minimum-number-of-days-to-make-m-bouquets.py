class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        #brute force solution

        # if m*k > len(bloomDay):
        #     return -1

        # low = min(bloomDay)
        # high = max(bloomDay)

        # for day in range(low,high+1):
        #     flower = 0
        #     bouquets = 0
        #     for bloom in bloomDay:
        #         if bloom<=day:
        #             flower += 1

        #             if flower == k:
        #                 bouquets += 1
        #                 flower = 0
        #         else:
        #             flower = 0

        #     if bouquets >= m:
        #         return day
        # return -1


        #optimal solution
        if m*k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1

        while low <= high :
            mid = (low+high)//2

            flower = 0
            bouquets = 0

            for bloom in bloomDay:
                if bloom <= mid:
                    flower += 1
                    if flower == k:
                        bouquets += 1
                        flower = 0
                else:
                    flower = 0
            if bouquets >= m:
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        return ans








        