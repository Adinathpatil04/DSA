class Solution(object):
    def minMoves(self, nums):
        max_val = max(nums)
        total_moves = 0
        
        for num in nums:
            total_moves += max_val - num
        
        return total_moves