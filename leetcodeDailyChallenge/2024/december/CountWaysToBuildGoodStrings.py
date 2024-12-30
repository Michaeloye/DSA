# https://leetcode.com/problems/count-ways-to-build-good-strings/

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        cache = {}

        def dfs(length):
            if length > high:
                return 0
            if length in cache:
                return cache[length]

            cache[length] = 1 if length >= low else 0
            cache[length] += dfs(length + zero) + dfs(length + one)

            return cache[length] % mod

        return dfs(0)