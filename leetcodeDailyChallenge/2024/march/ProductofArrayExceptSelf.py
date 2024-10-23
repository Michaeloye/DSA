# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]
        length = len(nums)
        
        leftMul = 1
        for i in range(0, length):
            if i == 0:
                res[0] = 1
                continue
            leftMul *= nums[i - 1]
            res[i] = leftMul
        
        rightMul = 1
        for j in range(length - 1, -1, -1):
            if j == length - 1:
                res[length - 1] *= 1
                continue
            rightMul *= nums[j + 1]
            res[j] *= rightMul
        
        return res


