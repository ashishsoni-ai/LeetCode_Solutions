class Solution:

    def solveSmaller(self, AssumedMid, mat):
        count = 0

        for i in range(len(mat)):
            start = 0
            end = len(mat[i]) - 1

            while start <= end:
                mid = (start + end) // 2

                if mat[i][mid] <= AssumedMid:
                    start = mid + 1
                else:
                    end = mid - 1

            count += start

        return count

    def median(self, mat):
        R = len(mat)
        C = len(mat[0])

        N = R * C
        medianIndex = (N // 2) + 1

        start = 1
        end = 2000

        while start <= end:
            AssumedMid = (start + end) // 2

            CurrentSmaller = self.solveSmaller(AssumedMid, mat)

            if CurrentSmaller < medianIndex:
                start = AssumedMid + 1
            else:
                end = AssumedMid - 1

        return start