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
