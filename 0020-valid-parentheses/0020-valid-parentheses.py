class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in mapping.values():
                stack.append(c)
            else:
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()

        return len(stack) == 0