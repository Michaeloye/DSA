# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    # solution 1
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Map = {nums2[-1]: -1}

        for i in range(len(nums2) - 1):
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i]:
                    nums2Map[nums2[i]] = nums2[j]
                    break
                else:
                    nums2Map[nums2[i]] = -1

        for j in range(len(nums1)):
            nums1[j] = nums2Map[nums1[j]]

        return nums1

    # Solution 2
    # O(nums1.length + nums2.length)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Map = {num: idx for idx, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]

            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1Map[val]
                res[idx] = curr

            if curr in nums1Map:
                stack.append(curr)

        return res
