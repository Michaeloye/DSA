class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        total = 0

        for i in range(len(nums)):
            
            if total > nums[i]:
                ans = total + nums[i]
            total += nums[i]
            


        return ans