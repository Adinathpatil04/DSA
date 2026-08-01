# class Solution(object):
#     def findPeakElement(self, nums):
#         i=0

#         for i in range(len(nums)):
#             if nums[i]>nums[i+1] and nums[i]>nums[i-1]:

#                 return i
        
class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)

        if n == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[n - 1] > nums[n - 2]:
            return n - 1

        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i