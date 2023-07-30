from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        length = len(arr)

        for i in range(length):
            for j in range(i + 1, length):
                if (arr[i] == arr[j] * 2 or arr[i] * 2 == arr[j]):
                    return True

        return False


soln = Solution()
arr = [10, 2, 5, 3]
print(soln.checkIfExist(arr))
