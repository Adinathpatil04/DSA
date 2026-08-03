class Solution(object):
    def singleNumber(self, nums):
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1

        for key in h:
            if h[key]==1:
                return key

