class Solution(object):
    def findTheDifference(self, s, t):
        XOR = 0

        for i in s:
            XOR ^= ord(i)

        for i in t:
            XOR ^= ord(i)

        return chr(XOR)