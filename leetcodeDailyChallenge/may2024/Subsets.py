# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, ds, res):
            if i == len(nums):
                res.append(ds[:])
                return
            
            # pick
            ds.append(nums[i])
            dfs(i + 1, ds, res)

            # don't pick
            ds.pop()
            dfs(i + 1, ds, res)
        
        ans = []
        dfs(0, [], ans)
        return ans