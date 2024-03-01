# https://leetcode.com/problems/rearrange-array-elements-by-sign

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negativeArr = []
        positiveArr = []
        res = []

        for num in nums:
            if num < 0:
                negativeArr.append(num)
            else:
                positiveArr.append(num)
        
        for i in range(len(negativeArr)):
            res.append(positiveArr[i])
            res.append(negativeArr[i])

        return res
