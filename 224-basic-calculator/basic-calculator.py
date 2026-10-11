class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        st = []
        number = 0
        result = 0
        sign = 1

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char == "+":
                result += number*sign
                sign = 1
                number = 0
             
            elif char == "-":
                result += number*sign
                sign = -1
                number = 0
              
            elif char == "(":
                st.append(result)
                st.append(sign)
                sign = 1
                number = 0
                result = 0
            elif char == ")":
                result += number*sign
                number = 0
                result *= st.pop()
                result += st.pop()
            
        result += number*sign
        return result
            


        