# https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        setNums1 = set(nums1)
        setNums2 = set(nums2)

        ans = setNums1.intersection(setNums2)
        return list(ans)