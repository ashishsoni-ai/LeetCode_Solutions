class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        arr = []

        for i in range(len(val)):
            arr.append((val[i] / wt[i], val[i], wt[i]))

        arr.sort(reverse=True)

        currW = 0
        finalValue = 0

        for i in range(len(arr)):
            if currW + arr[i][2] <= capacity:
                currW = currW + arr[i][2]
                finalValue = finalValue + arr[i][1]

            else:
                remain = capacity - currW
                cost = arr[i][0] * remain
                finalValue = finalValue + cost
                break

        return round(finalValue, 6)