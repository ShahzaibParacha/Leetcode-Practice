class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dict = {}
        for a in A:
            if a not in dict:
                dict[a] = 0 
            dict[a] += 1
            
        return max(dict, key=dict.get)

#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/