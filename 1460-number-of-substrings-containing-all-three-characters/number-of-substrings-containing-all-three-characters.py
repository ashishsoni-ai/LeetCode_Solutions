class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        last_seen = {"a": -1, "b": -1, "c": -1}
        count = 0

        for i in range(n):
            last_seen[s[i]] = i

            if (last_seen["a"] != -1 and
                last_seen["b"] != -1 and
                last_seen["c"] != -1):

                count += 1 + min(
                    last_seen["a"],
                    last_seen["b"],
                    last_seen["c"]
                )

        return count