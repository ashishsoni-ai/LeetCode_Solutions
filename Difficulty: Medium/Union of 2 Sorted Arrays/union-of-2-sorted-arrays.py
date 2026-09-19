class Solution:
    def findUnion(self, a, b):

        i = 0
        j = 0
        ans = []

        while i < len(a) and j < len(b):

            if a[i] < b[j]:

                if len(ans) == 0 or ans[-1] != a[i]:
                    ans.append(a[i])

                i += 1

            elif b[j] < a[i]:

                if len(ans) == 0 or ans[-1] != b[j]:
                    ans.append(b[j])

                j += 1

            else:

                if len(ans) == 0 or ans[-1] != a[i]:
                    ans.append(a[i])

                i += 1
                j += 1

        while i < len(a):

            if len(ans) == 0 or ans[-1] != a[i]:
                ans.append(a[i])

            i += 1

        while j < len(b):

            if len(ans) == 0 or ans[-1] != b[j]:
                ans.append(b[j])

            j += 1

        return ans