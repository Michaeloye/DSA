# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1

        for num in nums:
            prod = prod * num
            if prod == 0:
                break

        if prod >= 1:
            return 1
        if prod == 0:
            return 0

        return -1
