# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wCount = 0
        bCount = 0
        ans = float('inf')
        left  = 0

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                wCount += 1
            else:
                bCount += 1

            if right - left + 1 == k:
                # take count of "W" in that window, that's the number of Ws to change to black to have k consecutive
                ans = min(ans, wCount)
                if blocks[left] == 'W':
                    wCount -= 1
                else:
                    bCount -= 1
                left += 1
        return ans

# for max
class Solution1:
    def maximumRecolors(self, blocks: str, k: int) -> int:
        wCount = 0
        ans = 0
        left = 0

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                wCount += 1
            
            if right - left + 1 == k:
                ans = max(ans, wCount)

                if blocks[left] == 'W':
                    wCount -= 1
                left += 1

        return ans

sol1 = Solution1()
print(sol1.maximumRecolors("WBBWWBBWBW", 7))