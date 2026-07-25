class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row =len(matrix)
        col =len(matrix[0])
        row_track = [0]*row
        column_track = [0]*col

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    column_track[j] = -1

        for i in range(row):
            for j in range(col):
                if row_track[i] == -1 or column_track[j] == -1:
                    matrix[i][j] = 0

        