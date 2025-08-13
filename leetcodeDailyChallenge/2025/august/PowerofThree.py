# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        num = n

        while num > 1:
            if num % 3 == 0:
                num = num / 3
            else:
                return False

        return num == 1
