from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        slow = 0
        fast = 1
        length = len(arr)

        res = False
        hasReachedPeak = False

        if length <= 2:
            return res

        while fast < length:
            if arr[fast] == arr[slow]:
                return False

            elif arr[fast] > arr[slow]:
                if hasReachedPeak:
                    return False
                else:
                    res = True

            elif arr[fast] < arr[slow]:
                hasReachedPeak = True

            slow += 1
            fast += 1

        if hasReachedPeak:
            return res

        return False


soln = Solution()
arr = [0, 1, 2]

print(soln.validMountainArray(arr))
