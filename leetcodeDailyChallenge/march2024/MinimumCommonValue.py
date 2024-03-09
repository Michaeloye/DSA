# https://leetcode.com/problems/minimum-common-value/description/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] > nums1[i]:
                    break
                elif nums2[j] == nums1[i]:
                    return nums1[i]

        return -1

