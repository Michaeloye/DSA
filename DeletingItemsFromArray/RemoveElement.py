from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        notK = 0
        i = 1

        while i <= length:
            print(i)
            if nums[i-1] == val and i != length - 1:
                for j in range(i, length):
                    nums[j-1] = nums[j]

                # if (nums[i+1] == nums[i]):
                #     notK -= 1

                notK += 1
                i -= 1
                nums[length-1] = -1000
            elif i == length - 1:
                nums[i] = -10000
                notK += 1
            i += 1

        k = length - notK
        print(nums[0:k])


soln = Solution()
# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2
nums = [0, 0]
val = 0
soln.removeElement(nums, val)
