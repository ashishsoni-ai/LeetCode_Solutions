class Solution:
    def extractMaximum(self,s): 
        # code here
        maximum = -1
        current = 0
        in_number = False

        for ch in s:
            if ch.isdigit():
                current = current*10 + int(ch)
                in_number = True
            else:
                if in_number:
                    maximum = max(maximum, current)
                    current = 0
                    in_number = False

        if in_number:
            maximum = max(maximum, current)

        return maximum
        