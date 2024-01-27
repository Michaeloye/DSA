# https://leetcode.com/problems/k-inverse-pairs-array

# BRUTE FORCE
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        allPermutations = []

        def generate_permutations(elements, current_permutation=[]):
            if not elements:
                # If no elements left, one permutation is complete
                allPermutations.append([*current_permutation])
            else:
                # Iterate through each element and recursively find permutations
                for i in range(len(elements)):
                    remaining_elements = elements[:i] + elements[i + 1:]
                    new_permutation = current_permutation + [elements[i]]
                    generate_permutations(remaining_elements, new_permutation)

        generate_permutations([i for i in range(1, n + 1)])

        ans = 0
        for perm in allPermutations:
            pairCount = 0
            for i in range(len(perm)):
                for j in range(i, len(perm)):
                    if perm[i] > perm[j]:
                        pairCount += 1
            if pairCount == k:
                ans += 1
        return ans


# RECURSIVE

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        cache = {}

        def count(n, k):
            if n == 0:
                return 1 if k == 0 else 0
            if k < 0:
                return 0
            if (n, k) in cache:
                return cache[(n, k)]

            cache[(n, k)] = 0
            for i in range(n):
                cache[(n, k)] = (cache[(n, k)] + count(n - 1, k - i)) % MOD

            return cache[(n, k)]

        return count(n, k)


# DP

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 1

        for N in range(1, n + 1):
            for K in range(k + 1):
                for pairs in range(N):
                    if K - pairs >= 0:
                        dp[N][K] += dp[N - 1][K - pairs]

        return dp[n][k]


# SPACE OPTIMIZED DP

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        prev = [0] * (k + 1)

        prev[0] = 1

        for N in range(1, n + 1):
            cur = [0] * (k + 1)
            for K in range(k + 1):
                for pairs in range(N):
                    if K - pairs >= 0:
                        cur[K] += prev[K - pairs]

            prev = cur

        return prev[k]


# OPTIMAL DP SOLUTION
# https://leetcode.com/problems/k-inverse-pairs-array/submissions/1158512871/?envType=daily-question&envId=2024-01-27

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        prev = [0] * (k + 1)

        prev[0] = 1

        for N in range(1, n + 1):
            cur = [0] * (k + 1)
            total = 0  # sliding window
            for K in range(0, k + 1):
                if K >= N:
                    total -= prev[K - N]
                total = (total + prev[K]) % MOD
                cur[K] = total

            prev = cur

        return prev[k]
