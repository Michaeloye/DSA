# https://leetcode.com/problems/climbing-stairs/description/

# RECURSIVE SOLUTION
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(steps, ans):
            if steps > n:
                return 0
            if steps == n:
                print(steps)
                return ans + 1

            left = dfs(steps + 1, ans)
            right = dfs(steps + 2, ans)
            return left + right

        return dfs(0, 0)


# DP SOLUTION
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one
