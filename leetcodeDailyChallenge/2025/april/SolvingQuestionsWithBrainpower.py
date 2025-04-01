# https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        cache = {}
        def backtrack(i):
            if i >= len(questions):
                return 0
            if i in cache:
                return cache[i]

            points, brainpower = questions[i]

            cache[i] = max(
                backtrack(i + 1),
                points + backtrack(i + 1 + brainpower)
            )

            return cache[i]
        
        return backtrack(0)