# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rankOrder = sorted(arr)
        orderMap = {}
        ans = []
        rank = 1

        for num in rankOrder:
            if num not in orderMap:
                orderMap[num] = rank
                rank += 1
        
        for num in arr:
            ans.append(orderMap[num])
        return ans