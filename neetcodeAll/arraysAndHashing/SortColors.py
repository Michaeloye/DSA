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


# another Approach : Dutch National Flag algorithm
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
