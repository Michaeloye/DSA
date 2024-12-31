# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [(pos, v) for pos, v in zip(position, speed)]
        car.sort()
        car.reverse()

        times = [(target - pos) / v for pos, v in car]
        stack = []
        for t in times:
            if stack and t <= stack[-1]:
                continue
            stack.append(t)

        return len(stack)