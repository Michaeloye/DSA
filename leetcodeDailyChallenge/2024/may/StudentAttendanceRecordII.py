# https://leetcode.com/problems/student-attendance-record-ii/

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        cache = {}

        def count(n):
            if n == 1:
                return {
                    (0, 0): 1, (0, 1): 1, (0, 2): 0,
                    (1, 0): 1, (1, 1): 0, (1, 2): 0
                }
            if n in cache:
                return cache[n]
            tmp = count(n - 1)
            res = defaultdict(int)

            # choose p
            res[(0, 0)] = ((tmp[(0, 0)] + tmp[(0, 1)]) % MOD + tmp[(0, 2)]) % MOD
            res[(1, 0)] = ((tmp[(1, 0)] + tmp[(1, 1)]) % MOD + tmp[(1, 2)]) % MOD

            # choose l
            res[(0, 1)] = tmp[(0, 0)]
            res[(1, 1)] = tmp[(1, 0)]
            res[(0, 2)] = tmp[(0, 1)]
            res[(1, 2)] = tmp[(1, 1)]

            # choose a
            res[(1, 0)] = (res[(1, 0)] + (((tmp[(0, 0)] + tmp[(0, 1)]) % MOD + tmp[(0, 2)])) % MOD) % MOD

            cache[n] = res
            return res
        
        return sum(count(n).values()) % MOD