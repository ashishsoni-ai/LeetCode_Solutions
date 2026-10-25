class Solution:
    def solve(self,digits,subset,result,index,char_map):
        if len(subset) >= len(digits):
            result.append("".join(subset))
            return 
        for char in char_map[digits[index]]:
            subset.append(char)
            self.solve(digits,subset,result,index+1,char_map)
            subset.pop()
    def letterCombinations(self, digits: str) -> list[str]:
        subset = []
        result = []
        index = 0
        char_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        self.solve(digits,subset,result,index,char_map)
        return result
        