from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def mergeSort(array):
            if len(array) <= 1:
                return

            mid = len(array) // 2
            leftPart = array[0: mid]
            rightPart = array[mid: len(array)]

            mergeSort(leftPart)
            mergeSort(rightPart)
            merge(leftPart, rightPart, array)

        def merge(leftArray, rightArray, array):

            leftSize = len(leftArray)
            rightSize = len(rightArray)

            i, l, r = 0, 0, 0

            while (l < leftSize and r < rightSize):
                strLeft = str(leftArray[l])
                strRight = str(rightArray[r])
                if strLeft[0] == strRight[0]:
                    strComb1 = strLeft + strRight
                    strComb2 = strRight + strLeft

                    if int(strComb1) >= int(strComb2):
                        array[i] = leftArray[l]
                        l += 1
                    else:
                        array[i] = rightArray[r]
                        r += 1

                elif int(strLeft[0]) > int(strRight[0]):
                    array[i] = leftArray[l]
                    l += 1
                else:
                    array[i] = rightArray[r]
                    r += 1

                i += 1

            while l < leftSize:
                array[i] = leftArray[l]
                l += 1
                i += 1

            while r < rightSize:
                array[i] = rightArray[r]
                r += 1
                i += 1

        mergeSort(nums)
        return str(int("".join([str(num) for num in nums])))
