class Solution(object):
    def thirdMax(self, nums):
        
        s=set(nums)

        if len(s)<3:
            return max(s)

        else:
            s=list(s)
            s.sort()
            print(s)

            return s[-3]