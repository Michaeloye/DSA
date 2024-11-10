# https://leetcode.com/problems/minimum-array-end/

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        i_n = 1
        i_x = 1
        
        while i_n <= n - 1:
            if x & i_x == 0:
                if i_n & (n-1):
                    res = res | i_x
                i_n = i_n << 1
            i_x = i_x << 1
        return res

        # or
        for i in range(n - 1):
            res += 1
            res = res | x
        return res