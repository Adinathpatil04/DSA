class Solution(object):
    def isSubsequence(self, s, t):
        s = list(s)
        t = list(t)

        j = 0

        if len(s) == 0:
            return True

        for i in t:
            if j < len(s) and i == s[j]:
                j += 1

            if len(s) == j:
                return True

        return False