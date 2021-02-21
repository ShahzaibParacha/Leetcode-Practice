class Solution:
#    def helper(self, i, n):
#        if i > n:
#            return 0
#       if i == n:
#            return 1
#        else:
#            return self.helper(i+1, n) + self.helper(i+2, n)
#        
#    def climbStairs(self, n: int) -> int:
#        return self.helper(0, n)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        data = [0] * n
        data[0] = 1
        data[1] = 2
        for i in range(2,n):
            data[i] = data[i-1] + data[i-2]
            print(data[i])
            
        return data[n-1]
             