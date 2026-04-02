class Solution(object):
    def addDigits(self, num):
        # Continue until 'num' is a single digit
        while num >= 10:
            ans = 0
            while num != 0:
                r = num % 10    # Get last digit
                ans = ans + r   # Add to running total
                num = num // 10 # Remove last digit
            num = ans           # Update num with the sum for the next loop
            
        return num