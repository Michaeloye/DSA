# https://leetcode.com/problems/maximum-xor-for-each-query/description/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0

        for n in nums:
            xor ^= n
        
        answer = []
        mask = (1 << maximumBit) - 1

        for n in nums[::-1]:
            maxXor = mask ^ xor
            answer.append(maxXor)

            xor ^= n

        return answer