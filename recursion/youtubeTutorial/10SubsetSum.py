nums = [3, 1, 2, 5]

ans = []

def subsetSum(idx, currSum):
  if idx == len(nums):
    ans.append(currSum)
    return

  # pick
  currSum = currSum + nums[idx]
  subsetSum(idx + 1, currSum)

  # don't pick
  currSum = currSum - nums[idx]
  subsetSum(idx + 1, currSum)

subsetSum(0, 0)
ans.sort()
print(ans)

# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def uniqueSet(idx, subset):
            if idx == len(nums):
                ans.append([*subset])
                return

            # pick
            subset.append(nums[idx])
            uniqueSet(idx + 1, subset)

            # don't pick
            subset.pop()
            uniqueSet(idx + 1, subset)

        uniqueSet(0, [])
        return ans
