class Solution(object):
    def toLowerCase(self, s):
        s=list(s)

        ans=""
        for i in s:
            if i>='A' and i<='Z':
                ans=ans+chr(ord(i)+32)

            else:
                ans=ans+i

        return ans 
        