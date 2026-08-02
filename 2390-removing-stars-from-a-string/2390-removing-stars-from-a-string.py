class Solution(object):
    def removeStars(self, s):
        a = []

        for i in s:
            if i != "*":
                a.append(i)
            else:
                a.pop()

        s = ""
        for i in a:
            s += i

        return s