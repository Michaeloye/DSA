# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        array1 = version1.split(".")
        array2 = version2.split(".")

        diff = abs(len(array1) - len(array2))

        if len(array1) < len(array2):
            array1 = array1 + ( ['0'] * diff )
        elif len(array2) < len(array1):
            array2 = array2 + (['0'] * diff)
        
        for i in range(len(array1)):
            curr1 = int(array1[i])
            curr2 = int(array2[i])

            if curr1 < curr2:
                return -1
            if curr1 > curr2:
                return 1
        return 0