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