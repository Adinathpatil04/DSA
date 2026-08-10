class Solution(object):
    def peakIndexInMountainArray(self, arr):
        count = 0

        for i in range(1, len(arr) - 1):
            if (arr[i] > arr[i-1]) and (arr[i] > arr[i+1]):
                return i

        return 0