# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join([str(a) for a in digits])
        num = str(int(num) + 1)
        return [int(a) for a in num]
