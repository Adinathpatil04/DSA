class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False

        copy = x
        rev = 0

        while x != 0:
            r = x % 10
            rev = rev * 10 + r
            x = x // 10

        return copy == rev