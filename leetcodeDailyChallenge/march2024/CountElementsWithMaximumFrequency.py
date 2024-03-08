# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        numsMap = {} # num -> freq
        freqMap = {} # freq -> [nums]

        for num in nums:
            numsMap[num] = 1 + numsMap.get(num, 0)
        
        for num, freq in numsMap.items():
            if freq in freqMap:
                freqMap[freq].append(num)
            else:
                freqMap[freq] = [num]
        
        maxFreq = max(freqMap.keys())
        return len(freqMap[maxFreq]) * maxFreq