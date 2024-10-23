# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        res = 0

        for i in range(len(nums)):
            while q and i > q[0] + k - 1:
                q.popleft()

            if (len(q) + nums[i]) % 2 == 0:
                if i + k > len(nums):
                    return -1
                res += 1
                q.append(i)

        return res