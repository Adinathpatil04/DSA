class Solution(object):
    def largestAltitude(self, gain):
        sum = 0
        m = 0

        for i in range(len(gain)):
            sum += gain[i]
            m = max(m, sum)

        return m