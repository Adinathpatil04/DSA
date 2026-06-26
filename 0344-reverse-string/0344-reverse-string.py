class Solution(object):
    def reverseString(self, str):
        i = 0
        j = len(str) - 1

        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1