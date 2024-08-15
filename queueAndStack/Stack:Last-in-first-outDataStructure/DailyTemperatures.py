class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [idx, temp]
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIdx, _ = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([i, temp])
        return res
