class Solution(object):
    def mergeAlternately(self, a, b):
        i=0
        j=0

        ans=""
        x=min(len(a),len(b))

        for i in range(0,x-1+1,1):
            ans= ans+ a[i]+ b[i]

        ans= ans + a[x: ]
        ans = ans+ b[x: ]

        return ans
        