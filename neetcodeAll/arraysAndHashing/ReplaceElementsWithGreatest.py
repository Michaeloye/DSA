# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        i = length - 1
        maxNum = -1

        while i >= 0:
            tmp = arr[i]
            arr[i] = maxNum

            if (tmp > maxNum):
                maxNum = tmp
            i -= 1

        return arr
