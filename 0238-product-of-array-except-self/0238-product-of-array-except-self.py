class Solution(object):
    def productExceptSelf(self, nums):
        psum = [1 for i in range(len(nums))]

        prod = 1

        for i in range(len(nums)):
            psum[i] = prod
            prod = prod * nums[i]

        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            psum[i] = psum[i] * prod
            prod = prod * nums[i]

        return psum