# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Count = defaultdict(int)
        nums2Count = defaultdict(int)
        ans = []

        for num in nums1:
            nums1Count[num] += 1
        for num in nums2:
            nums2Count[num] += 1
        
        minNumsCount = {}

        if len(nums1Count) <= len(nums2Count):
            minNumsCount = nums1Count
        else:
            minNumsCount = nums2Count

        for num in minNumsCount:
            minNum = min(nums1Count[num], nums2Count[num])
            for i in range(minNum):
                ans.append(num)

        return ans