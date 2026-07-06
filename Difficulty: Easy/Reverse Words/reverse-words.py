class Solution:
    def reverseWords(self, s):
        # code here
        words = []
        for word in s.split("."):
            if word != "":
                s = words.append(word)
        words.reverse()
        return ".".join(words)