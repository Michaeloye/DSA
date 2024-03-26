# https://leetcode.com/problems/4sum

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = []

        for i in range(N - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, N - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = N - 1

                while l < r:
                    fourSum = nums[i] + nums[j] + nums[l] + nums[r]

                    if fourSum > target:
                        r -= 1
                    elif fourSum < target:
                        l += 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return ans


# recursive solution
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []
        subRes = []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, N - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    subRes.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    subRes.pop()
                return
            
            # base case
            l = start
            r = N - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append(subRes + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        kSum(4, 0, target)
        return res