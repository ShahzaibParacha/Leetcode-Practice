class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        reverse = ""
        if x[0] == "-":
            reverse += x[0]
            reverse += x[::-1]
            reverse = reverse[:-1]
        else:
            reverse = x[::-1]
        
        reverse = int(reverse)
        
        if reverse < (pow(2, 31) -1) and reverse > -pow(2,31):
            return reverse
        return 0
            
        
            