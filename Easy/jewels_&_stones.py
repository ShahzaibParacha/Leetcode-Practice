class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        tokens = list(J)
        s = list(S)
        count=0
        for i in s:
            if i in tokens:
                count+=1
        return count

#https://leetcode.com/problems/jewels-and-stones/