class Solution(object):
    def isIsomorphic(self, s, t):

        h={}
        s=list(s)
        t=list(t)
        for i in range (0,len(s),1):
            if s[i] in h.keys() and h[s[i]] != t[i]:
                return False
            elif s[i] not in h.keys() and t[i] in h.values():
                return False

            else:
                h[s[i]] = t[i]
        return True
        