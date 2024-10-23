# https://leetcode.com/problems/the-number-of-beautiful-subsets/

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = []
        ds = []
        nums.sort()
        def dfs(i):
            if i == len(nums):
                if len(ds) > 1:
                    l = 0
                    r = 1
                    while r < len(ds):
                        if ds[r] - ds[l] > k:
                            l += 1
                        elif ds[r] - ds[l] < k:
                            r += 1
                        else:
                            return
                res.append(ds[:])
                return
            
            # pick
            ds.append(nums[i])
            dfs(i + 1)

            # don't pick
            ds.pop()
            dfs(i + 1)
        dfs(0)
        return len(res) - 1