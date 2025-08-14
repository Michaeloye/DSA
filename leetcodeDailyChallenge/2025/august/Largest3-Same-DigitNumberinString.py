# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans = -1
        for i in range(1, len(num) - 1):
            prev_num = num[i - 1]
            cur_num = num[i]
            next_num = num[i + 1]

            if prev_num == cur_num == next_num:
                ans = max(ans, int(cur_num * 3))
        
        if ans == -1:
            return ""
        elif ans == 0:
            return "000"
        else:
            return str(ans)