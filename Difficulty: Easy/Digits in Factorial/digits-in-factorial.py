import math

class Solution:
    def digitsInFactorial(self, N):
        if N <= 1:
            return 1

        digits = (
            N * math.log10(N / math.e)
            + math.log10(2 * math.pi * N) / 2
        )

        return int(digits) + 1