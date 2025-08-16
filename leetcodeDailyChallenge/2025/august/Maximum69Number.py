# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = num
        num_str = str(num)

        for i in range(len(num_str)):
            left = num_str[:i]
            cur = num_str[i]
            right = num_str[i + 1:]

            if cur == "6":
                new_num = int(left + "9" + right)
                ans = max(ans, new_num)

        return ans
