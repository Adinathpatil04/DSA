class Solution(object):
    def reverseWords(self, s):
        s=s.strip()
        a=s.split(' ')
        print(a)


        ans=""
        x=len(a)

        i=len(a)-1
        while i>0:
            if len(a[i])>0:
                ans=ans+a[i]+" "
            i=i-1

        ans=ans+a[0]
        print(ans)
        return ans
        