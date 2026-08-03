import math

class Solution:
    def numOfPerfectSquares(self, a, b):
        start = math.ceil(math.sqrt(a))
        end = math.floor(math.sqrt(b))
        
        return end - start + 1 if start <= end else 0