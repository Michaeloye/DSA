# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        possibleArr = set(list(range(1, n + 1)))

        # remove banned
        for n in banned:
            if n in possibleArr:
                possibleArr.remove(n)
        
        possibleArr = list(possibleArr)
        possibleArr.sort()

        ans = 0

        for n in possibleArr:
            maxSum -= n
            if maxSum < 0:
                break
            ans += 1
        return ans


# O(n) solution
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        ans = 0

        for n in range(1, n + 1):
            if n in banned:
                continue
            maxSum -= n
            if maxSum < 0:
                return ans
            ans += 1
        return ans
