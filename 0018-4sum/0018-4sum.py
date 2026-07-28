class Solution(object):
    def fourSum(self, nums, target):
        a=nums
        a.sort()
        h = set()

        i = 0
        while i < len(nums) - 3:
            j = i + 1

            while j < len(nums) - 2:
                k = j + 1
                l = len(nums) - 1

                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]

                    if s == target:
                        h.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif s > target:
                        l -= 1
                    else:
                        k += 1

                j += 1

            i += 1

        return [list(x) for x in h]