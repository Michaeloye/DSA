# https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        topK = []

        for i in nums:
            if i in numsMap:
                numsMap[i] += 1
            else:
                numsMap[i] = 1

        while k > 0 and len(numsMap) != 0:
            topK.append(self.getMaxInMap(numsMap))
            k -= 1

        return topK

    def getMaxInMap(self, hashMap):

        maxkey = 0
        maxVal = 0
        for key in hashMap:
            if hashMap[key] > maxVal:
                maxkey = key
                maxVal = hashMap[key]

        del hashMap[maxkey]
        return maxkey


# buckek approach
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucketList = [[] for _ in range(len(nums) + 1)]
        numsCountMap = {}
        res = []

        for i in nums:
            numsCountMap[i] = 1 + numsCountMap.get(i, 0)

        for key in numsCountMap:
            bucketList[numsCountMap[key]].append(key)

        for i in range(len(bucketList) - 1, 0, -1):
            for j in bucketList[i]:
                if k > 0:
                    res.append(j)
                    k -= 1
        return res
