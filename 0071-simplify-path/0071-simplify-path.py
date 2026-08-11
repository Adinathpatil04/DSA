class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        lst = path.split("/")
        print(lst)
        curr = "."
        prev_dir=".."
        res = []    
        for i,val in enumerate(lst):

            if len(val)>0:
                if val == prev_dir:
                    if len(res)>0:
                        res.pop()
                        
                elif val == curr:
                    continue
                else:
                    res.append(val)
        result="/"+"/".join(res)
        return result
     

