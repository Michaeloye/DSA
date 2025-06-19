# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

class Solution:
  def partitionArray(self, nums, k):
    nums.sort()

    start = 0
    ans = 0
    arr = []

    for end in range(len(nums)):
      if nums[end] - nums[start] <= k:
        continue
      else:
        ans += 1
        start = end
        arr.append(nums[start:end])

    return ans + 1