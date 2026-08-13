class Solution(object):
    def mergeAlternately(self, a, b):
        m=min(len(a),len(b))
        ans=""
        for i in range(0,m-1+1,1):
            ans=ans+a[i]+b[i]

        ans=ans+a[m:]
        ans=ans+b[m:]

        return ans
       