class Solution:

    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        stack = []

        for num in asteroids:

            while len(stack) != 0 and stack[-1] > 0 and num < 0 and stack[-1] < abs(num):
                stack.pop()

            if len(stack) != 0 and stack[-1] > 0 and num < 0:

                if stack[-1] == abs(num):
                    stack.pop()

                # stack top is bigger, so current asteroid is destroyed
                elif stack[-1] > abs(num):
                    continue

            else:
                stack.append(num)

        return stack