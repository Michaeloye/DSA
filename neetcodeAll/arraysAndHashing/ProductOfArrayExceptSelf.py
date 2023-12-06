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
