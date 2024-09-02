# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0
        n = len(chalk)  
        chalkSum = sum(chalk)
        k = k % chalkSum

        while True:
            if chalk[i] > k:
                return i

            k -= chalk[i]
            i += 1
            i %= n