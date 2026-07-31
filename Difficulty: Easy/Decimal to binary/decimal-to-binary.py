class Solution:
    def decToBinary(self, n):
        # code here
        ans = ""
        while n>0:
            if n%2 == 1:
                ans += "1"
            else:
                ans += "0"
            n = n//2
        ans = ans[::-1]
        return int(ans)
        