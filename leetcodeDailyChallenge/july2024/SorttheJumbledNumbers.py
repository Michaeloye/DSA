# https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []

        for i, n in enumerate(nums):
            n = str(n)
            mappedN = 0

            for num in n:
                mappedN *= 10
                mappedN += mapping[int(num)]
            
            pairs.append((mappedN, i))

        pairs.sort()

        return [nums[pair[1]] for pair in pairs]