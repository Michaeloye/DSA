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

# more optimal solution
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        index1 = 0
        index2 = 0
        
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                return nums1[index1]
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1

        return -1