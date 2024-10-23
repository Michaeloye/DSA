# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
        
        return ans

# add another method O(n) using bucket sort
# constraint has it that height[i] is range 1 to 100
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = []
        bucket = [[] for _ in range(100)]

        for n in heights:
            bucket[n - 1].append(n)
        
        for item in bucket:
            for n in item:
                expected.append(n)

        ans = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
        
        return ans