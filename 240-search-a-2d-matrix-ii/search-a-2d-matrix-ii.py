class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        TotalRows = len(matrix)
        TotalColumns = len(matrix[0])
        row = 0
        col = TotalColumns-1
        while row<TotalRows and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
        