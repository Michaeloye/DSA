# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numMap = {0: 0}
        maxVal = 0
        result = 0
        for i in nums:
            if i in numMap:
                numMap[i] = numMap[i] + 1
            else:
                numMap[i] = 1

            result = i if numMap[i] > maxVal else result
            maxVal = max(numMap[i], maxVal)

        return result

    # boyer-moore algorithm in 0(n) time and 0(1) space
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        result = nums[0]

        for i in range(1, len(nums)):
            if count <= 0:
                result = nums[i]

            if nums[i] != result:
                count -= 1
            else:
                count += 1

        return result
