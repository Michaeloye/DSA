# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        
        num = n
        while num > 1:
            if num % 4 == 0:
                num = num / 4
            else:
                return False
        
        return True if num == 1 else False
