from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        i = length - 1
        maxNum = 0

        while i >= 0:
            tmp = arr[i]
            arr[i] = maxNum

            if (i == length - 1):
                arr[i] = -1

            if (tmp > maxNum):
                maxNum = tmp
                print(maxNum)

            i -= 1

        return arr
