# https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quickSort(array, start, end):

            if end <= start:
                return

            pivot = array[end]
            i = start - 1

            for j in range(start, end + 1):
                if array[j] < pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]

            i += 1
            array[i], array[j] = array[j], array[i]

            quickSort(array, start, i - 1)
            quickSort(array, i + 1, end)

        quickSort(nums, 0, len(nums) - 1)
