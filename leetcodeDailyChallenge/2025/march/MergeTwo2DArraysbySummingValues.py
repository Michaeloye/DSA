# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        left = 0
        right = 0
        ans = []

        while left < len(nums1) and right < len(nums2):
            if nums1[left][0] == nums2[right][0]:
                ans.append([nums1[left][0], nums1[left][1] + nums2[right][1]])
                left += 1
                right += 1
            elif nums1[left][0] < nums2[right][0]:
                ans.append(nums1[left])
                left += 1
            else:
                ans.append(nums2[right])
                right += 1

        while left < len(nums1):
            ans.append(nums1[left])
            left += 1

        while right < len(nums2):
            ans.append(nums2[right])
            right += 1

        return ans