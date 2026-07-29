class Solution(object):
    def mergeAlternately(self, word1, word2):
        i = 0
        j = 0
        x = 0
        c = ""

        while i < len(word1) and j < len(word2):
            if x % 2 == 0:
                c += word1[i]
                i += 1
            else:
                c += word2[j]
                j += 1
            x += 1

        while i < len(word1):
            c += word1[i]
            i += 1

        while j < len(word2):
            c += word2[j]
            j += 1

        return c