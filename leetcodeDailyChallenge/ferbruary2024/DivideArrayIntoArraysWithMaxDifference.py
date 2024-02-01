# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        count = 0

        for i in range(len(nums)):
            num = nums[i]

            if count == 0:
                ans.append([num])
            else:
                # since its sorted definitely the last element is the smallest
                # so if num - smallest num > k then a condition is not met as indicated in the problem
                refNum = ans[-1][0]
                diff = num - refNum    

                if diff > k:
                    return []
                ans[-1].append(num)

            count = (count + 1) % 3

        return ans