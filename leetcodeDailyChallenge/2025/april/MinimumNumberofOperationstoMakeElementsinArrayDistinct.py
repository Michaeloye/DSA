# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = {}
        ans = 0

        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i], 0)
        for k in range(len(nums)):
            if k % 3 == 0:
                if sum(counter.values()) == len(counter):
                    return ans

                ans += 1
            counter[nums[k]] -= 1
            if counter[nums[k]] == 0:
                counter.pop(nums[k])

        return ans


# better solution
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = {}

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in counter:  
                return (i // 3) + 1
            else:
                counter[nums[i]] = 1 + counter.get(nums[i], 0)
        return 0
            
        