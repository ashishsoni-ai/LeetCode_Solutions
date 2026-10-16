class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []

        for i in range(n-1,-1,-1):
            while len(stack) > 0 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if len(stack) == 0:
                result[i] = 0
            else:
                result[i] = stack[-1] - i

            stack.append(i)

        return result


        