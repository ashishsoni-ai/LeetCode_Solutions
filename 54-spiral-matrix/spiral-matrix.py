class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        
        total = n*m
        ans = []
        c =0
        RowStart = 0
        ColStart = 0
        RowEnd  = n-1
        ColEnd = m-1
        while c<total:

            for i in range(ColStart,ColEnd+1):
                ans.append(matrix[RowStart][i])
                c+=1
            RowStart += 1
            if c==total:
                break

            for i in range(RowStart,RowEnd+1):
                ans.append(matrix[i][ColEnd])
                c+=1
            ColEnd -= 1
            if c==total:
                break

            for i in range(ColEnd,ColStart-1,-1):
                ans.append(matrix[RowEnd][i])
                c+=1
            RowEnd -= 1
            if c==total:
                break

            for i in range(RowEnd,RowStart-1,-1):
                ans.append(matrix[i][ColStart])
                c+=1
            ColStart += 1
            
        return ans

        