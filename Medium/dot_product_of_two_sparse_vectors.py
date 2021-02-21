class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(self.data) == len(vec.data):
            index = 0
            dp = 0
            for i in range(len(self.data)):
                dp += self.data[i] * vec.data[i]
            return dp
        return -1
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)