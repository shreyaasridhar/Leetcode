class Solution(object):
    def numJewelsInStones(self, J, S):
        a= []
        ct=0
        for i in J:
            a.append(i)
        x=set(a)    
        for i in S:
            for j in x:
                if i==j:
                    ct+=1
        return ct