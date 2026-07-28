class Solution(object):
    def checkIfPangram(self, sentence):
        h={}

        # for chr in sentence:
        #     h[chr]=1

        # return len(h)==26
       

        for chr in sentence:
            if chr not in h:
                h[chr] = 1

        for chr in "abcdefghijklmnopqrstuvwxyz":
            if chr not in h:
                return False

        return True
            
                

        
