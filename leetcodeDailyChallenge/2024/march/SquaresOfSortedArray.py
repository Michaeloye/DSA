# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            ans.append(num * num)
        
        return sorted(ans)