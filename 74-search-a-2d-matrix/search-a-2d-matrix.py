class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        TotalRow = len(matrix)
        TotalColumn = len(matrix[0])
        n = TotalRow*TotalColumn
        start = 0
        end = n-1

        while start<=end:
            mid = (start+end)//2
            rowIndex = mid//TotalColumn
            colIndex = mid % TotalColumn
            if matrix[rowIndex][colIndex] == target:
                return True
            if matrix[rowIndex][colIndex] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


        