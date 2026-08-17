class Solution:
    def myAtoi(self, s: str, i=0, num=0, sign=1, started=False) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Skip spaces and find sign
        if not started:
            while i < len(s) and s[i] == ' ':
                i += 1

            if i < len(s) and s[i] == '-':
                sign = -1
                i += 1
            elif i < len(s) and s[i] == '+':
                i += 1

            started = True

        # Stop at end or non-digit
        if i >= len(s) or s[i] < '0' or s[i] > '9':
            return sign * num

        # Convert character to digit
        digit = ord(s[i]) - ord('0')

        # Build number
        num = num * 10 + digit

        # Check overflow
        if sign == 1 and num > INT_MAX:
            return INT_MAX

        if sign == -1 and -num < INT_MIN:
            return INT_MIN

        # Recursive call
        return self.myAtoi(s, i + 1, num, sign, started)