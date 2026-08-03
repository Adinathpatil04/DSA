class Solution(object):
    def isPossibleToSplit(self, nums):
        h={}

        for i in nums:
            if i in h.keys() and h[i]==2:
                return False

            elif i in h.keys():
                h[i]=h[i]+1

            else:
                h[i]=1
        return True


        