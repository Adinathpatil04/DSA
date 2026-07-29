class Solution(object):
    def firstMissingPositive(self, nums):
        h=set(nums)

        i=1

        while True:
            if i not in h:
                return i

            i=i+1



        