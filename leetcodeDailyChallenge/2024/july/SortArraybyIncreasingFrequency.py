# https://leetcode.com/problems/sort-array-by-increasing-frequency

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        countMap = Counter(nums)

        def customSort(n):
            return (countMap[n], -n)

        nums.sort(key=customSort)
        return nums
