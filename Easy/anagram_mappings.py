class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        out = []
        for a in A:
            if a in B:
                out.append(B.index(a))
        return out

#https://leetcode.com/problems/find-anagram-mappings/