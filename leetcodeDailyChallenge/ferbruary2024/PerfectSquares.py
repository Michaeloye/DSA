class Solution:
    def numSquares(self, n: int) -> int:
        res = n

        def root(num, ans):
            nonlocal res

            if num ** 2 > n or sum(ans) > n:
                return
            elif sum(ans) == n:
                res = min(res, len(ans) - 1)
                return

            for i in range(1, int(n ** 0.5) + 1):
                ans.append(num ** 2)
                root(i, ans)
                ans.pop()

        root(0, [])
        return res


#  OPTIMIZED SOLUTION
class Solution:
    def numSquares(self, n: int) -> int:
        cache = [n] * (n + 1)
        cache[0] = 0

        for i in range(1, n + 1):
            for s in range(1, i + 1):
                square = s * s

                if i - square < 0:
                    break
                if 1 + cache[i - square] < cache[i]:
                    cache[i] = 1 + cache[i - square]
        
        return cache[n]
    
