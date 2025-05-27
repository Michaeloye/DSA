# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1 = 0
        nums2 = 0

        for x in range(n + 1):
            if x % m != 0:
                nums1 += x
            else:
                nums2 += x

        return nums1 - nums2