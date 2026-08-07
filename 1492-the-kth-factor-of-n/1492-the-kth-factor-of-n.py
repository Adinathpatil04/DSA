class Solution(object):
    def kthFactor(self, n, k):
        f=[]

        for i in range(1,n+1,1):
            if n%i==0:
                f.append(i)

        
        if k>len(f):
            return -1
        else:
            return f[k-1]
        