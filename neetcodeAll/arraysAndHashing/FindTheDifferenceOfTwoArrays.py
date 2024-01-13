# https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        answer = [[], []]

        answer[0] = list(nums1.difference(nums2))
        answer[1] = list(nums2.difference(nums1))
        return answer
