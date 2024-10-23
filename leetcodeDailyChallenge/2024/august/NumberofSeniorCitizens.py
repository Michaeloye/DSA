# https://leetcode.com/problems/number-of-senior-citizens/

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        def isSeniorAge(detail):
            age = int(detail[11:13])
            return True if age > 60 else False

        ans = 0
        for detail in details:
            if isSeniorAge(detail):
                ans += 1

        return ans