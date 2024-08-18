# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        factors = [2, 3, 5]
        visited = set()

        heapq.heapify(minHeap)

        for i in range(n):
            num = heapq.heappop(minHeap)

            if i == n - 1:
                return num
            
            for factor in factors:
                prod = factor * num
                if prod not in visited:
                    visited.add(prod)
                    heapq.heappush(minHeap, prod)


# O(n) time
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2 = 0
        i3 = 0
        i5 = 0

        for i in range(1, n):
            newNum = min(
                nums[i2] * 2,
                nums[i3] * 3,
                nums[i5] * 5
            )

            if nums[i2] * 2 == newNum:
                i2 += 1

            if nums[i3] * 3 == newNum:
                i3 += 1

            if nums[i5] * 5 == newNum:
                i5 += 1

            nums.append(newNum)
        
        return nums[n - 1]