# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productArr = 1
        numsMap = {}
        for i in nums:
            numsMap[i] = 1 + numsMap.get(i, 0)

        if numsMap.get(0, 0) > 1:
            productArr = 0
        else:
            for i in nums:
                if i != 0:
                    productArr *= i
        for idx, num in enumerate(nums):
            if num == 0:
                nums[idx] = productArr
            elif num != 0 and numsMap.get(0, 0) > 0:
                nums[idx] = 0
            else:
                nums[idx] = productArr // num

        return nums


# another solution (without using division)
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
