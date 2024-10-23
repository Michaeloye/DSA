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


# O(n)
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numsMap = {} #Num: len

        for num in arr:
            numsMap[num] = 1 + numsMap.get(num, 0)

        bucket = [0 for i in range(len(arr) + 1)] # freq -> number of elements with that freq
        res = len(numsMap)

        for num in numsMap:
            val = numsMap[num]
            bucket[val] += 1
        
        for f in range(1, len(bucket)):
            remove = bucket[f]

            if k >= f * remove:
                k -= f * remove
                res -= remove
            else:
                remove = k // f
                res -= remove
                break
        return res