class Solution:
    def solve(self,index,numbers,result):
        if index == len(numbers):
            result.append("".join(numbers))
            return
        numbers[index] = "0"
        self.solve(index+1,numbers,result)
        numbers[index] = "1"
        self.solve(index+1,numbers,result)

    def binstr(self, n):
        # code here
        numbers = [0]*n
        result = []
        self.solve(0,numbers,result)
        return result
        
        