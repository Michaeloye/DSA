# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0 
        r = len(arr) - 1
        val = arr[0]
        idx = 0
        
        while l <= r:
            m = l + (r - l) // 2
            currDiff = abs(arr[m] - x)
            resDiff = abs(val - x)

            if currDiff < resDiff or (currDiff == resDiff and arr[m] < val):
                val, idx = arr[m], m
            
            if arr[m] < x:
                l = m + 1
            elif arr[m] > x:
                r = m - 1
            else:
                break


        l = idx
        r = idx
        
        for i in range(k - 1):
            if l == 0:
                r += 1
            elif r == len(arr) - 1 or x - arr[l - 1] <= arr[r + 1] - x:
                l -= 1
            else:
                r += 1
        return arr[l:r + 1]