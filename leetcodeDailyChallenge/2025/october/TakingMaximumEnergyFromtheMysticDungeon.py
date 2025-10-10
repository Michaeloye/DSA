# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        N = len(energy)
        dp = [0] * N

        for i in range(N-k, N):
            dp[i] = energy[i]

        for i in range(N - k - 1, -1, -1):
            dp[i] = dp[i + k] + energy[i]

        return max(dp)
