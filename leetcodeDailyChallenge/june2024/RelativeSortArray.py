# https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2Set = set(arr2)
        arr1Map = {}
        end = []
        ans = []
        for num in arr1:
            if num not in arr2Set:
                end.append(num)
            arr1Map[num] = 1 + arr1Map.get(num, 0)

        end.sort()

        for num in arr2:
            for _ in range(arr1Map[num]):
                ans.append(num)

        ans = ans + end
        return ans