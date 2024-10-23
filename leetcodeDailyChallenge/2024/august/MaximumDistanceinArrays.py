# https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # loop through get min and max for each subarr and assign to a variable

        curMin = arrays[0][0]
        curMax = arrays[0][-1]

        res = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]

            res = max(
                res,
                arr[-1] - curMin,
                curMax - arr[0]
            )

            curMin = min(curMin, arr[0])
            curMax = max(curMax, arr[-1])

        return res