# https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        setNums = set(nums)
        uniqueNums = set()
        ans = [1, 0]

        for i in range(n):
            val = nums[i]
            # check for duplicate number
            if val in uniqueNums:
                ans[0] = val

            # check for missing number
            if val + 1 <= n and val + 1 not in setNums:
                ans[1] = val + 1
            elif val - 1 > 0 and val - 1 not in setNums:
                ans[1] = val - 1
            uniqueNums.add(val)

        return ans

# second solution


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0, 0]
        duplicate = 0

        for i in range(n):
            idx = abs(nums[i])
            idx = idx - 1
            if nums[idx] < 0:
                duplicate = abs(nums[i])
                ans[0] = duplicate
            nums[idx] *= -1

        for i in range(n):
            if nums[i] > 0 and i + 1 != duplicate:
                ans[1] = i + 1
        return ans


# third solution
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        x = 0  # duplicate - missing
        y = 0  # duplicate^2 - missing^2

        for i in range(1, n + 1):
            x += nums[i - 1] - i
            y += nums[i - 1]**2 - i ** 2

        missing = (y - x**2) // (2 * x)
        duplicate = (missing) + x

        return [duplicate, missing]


# four solution using AP

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        expectedSum = n * (n + 1) // 2

        seen = set()
        duplicate = 0
        missing = 0

        actualSum = 0

        for num in nums:
            if num in seen:
                duplicate = num

            seen.add(num)
            actualSum += num

        missing = expectedSum - actualSum + duplicate

        return [duplicate, missing]
