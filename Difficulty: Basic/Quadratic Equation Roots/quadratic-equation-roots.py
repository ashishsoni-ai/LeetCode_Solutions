import math

class Solution:
    def quadraticRoots(self, a, b, c):
        d = b * b - 4 * a * c

        if d < 0:
            return [-1]

        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)

        r1 = math.floor(root1)
        r2 = math.floor(root2)

        if r1 >= r2:
            return [r1, r2]
        else:
            return [r2, r1]