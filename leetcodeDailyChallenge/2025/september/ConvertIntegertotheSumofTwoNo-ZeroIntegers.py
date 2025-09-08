# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # go from 1 to n (i)
        # add i to n - i
        # if both don't have any zeros return ans

        for i in range(1, n):
            j = n - i
            if "0" in str(i) or "0" in str(j):
                continue
            else:
                return [i, j]
        return []