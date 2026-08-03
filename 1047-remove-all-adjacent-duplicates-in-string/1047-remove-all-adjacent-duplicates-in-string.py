class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for i in s:
            if len(stack)>0 and stack[-1]==i:
                stack.pop()

            else:
                stack.append(i)

        s=""
        for i in stack:
            s=s+i
        return s

        