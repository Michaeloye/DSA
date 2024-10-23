# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        
        for i in range(n):
            currTemp = temperatures[i]
            idx, temp = stack[-1] if stack else (float("inf"), float("inf"))
            
            if temp >= currTemp:
                stack.append((i, currTemp))
            else:
                while stack:    
                    idx, temp = stack[-1]
                    if temp >= currTemp:
                        break
                    temperatures[idx] = i - idx
                    stack.pop()
                stack.append((i, currTemp))

        while stack:
            idx, temp = stack.pop()
            temperatures[idx] = 0
            
        return temperatures