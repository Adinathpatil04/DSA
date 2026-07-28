class Solution(object):
    def findDisappearedNumbers(self, nums):
        h={}
        ans=[]

        for num in nums:
            h[num]=1

        for i in range(1,len(nums)+1):
            if i not in h:
                ans.append(i)
        return ans
        
        