# https://leetcode.com/problems/greatest-common-divisor-traversal

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        if self.size[px] < self.size[py]:
            self.par[px] = py
            self.size[py] += self.size[px]
        else:
            self.par[py] = px
            self.size[px] += self.size[py]
        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        factorIdx = {} # f -> idx of value with factor f
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factorIdx:
                        uf.union(i, factorIdx[f])
                    else:
                        factorIdx[f] = i
                    while  n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in factorIdx:
                    uf.union(i, factorIdx[n])
                else:
                    factorIdx[n] = i

        return uf.count == 1


# shorter solution
# https://leetcode.com/problems/greatest-common-divisor-traversal/submissions/1186187041/
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums)==1:return True
        nums = set(nums)
        if 1 in nums:return False
        if len(nums)==1:return True
        
        nums = sorted(nums,reverse=True)

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if gcd(nums[i],nums[j])-1:
                    nums[j]*=nums[i]
                    break
            else:
                return False
        return True
