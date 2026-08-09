class Solution(object):
    def maxSubArray(self, nums):
        psum = [nums[0]]

        for i in range(1, len(nums)):
            x = max(psum[i-1] + nums[i], nums[i])
            psum.append(x)

        return max(psum)