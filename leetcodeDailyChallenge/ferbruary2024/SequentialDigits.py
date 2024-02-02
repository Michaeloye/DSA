# https://leetcode.com/problems/sequential-digits/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lowLen = len(str(low))
        highLen = len(str(high))
        nums = ["1","2","3","4","5","6","7","8","9"]
        ans = []
        for i in range(lowLen, highLen + 1):
            for j in range(len(nums)):
                subNum = int("".join(nums[j:j + i]))

                if subNum < low:
                    continue
                elif subNum > high or len(str(subNum)) < i:
                    break
                ans.append(subNum)

        return ans