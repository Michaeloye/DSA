# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numsMap = {} #Num: len

        for num in arr:
            numsMap[num] = 1 + numsMap.get(num, 0)

        freqs = sorted(numsMap.values())
        ans = len(freqs)

        for idx, num in enumerate(freqs):
            if k >= num:
                ans -= 1
                k -= num
            else:
                break
        return ans
