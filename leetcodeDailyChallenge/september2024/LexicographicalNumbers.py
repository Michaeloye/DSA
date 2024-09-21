# https://leetcode.com/problems/lexicographical-numbers/

# recursive
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(cur):
            if cur > n:
                return
            
            res.append(cur)
            cur = cur * 10

            for i in range(10):
                dfs(cur + i)
        
        for i in range(1, 10):
            dfs(i)

        return res

# iterative
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        cur = 1

        while len(res) < n:
            res.append(cur)

            if cur * 10 <= n:
                cur *= 10
            else:
                while cur == n or cur % 10 == 9:
                    cur = cur // 10
                cur += 1
        return res