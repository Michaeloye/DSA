# https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_n = [0] * (n + 1)
        postfix_y = [0] * (n + 1)

        min_penalty = n + 1
        min_penalty_idx = 0

        for i in range(1, n + 1):
            prefix_n[i] = prefix_n[i - 1]
            if customers[i - 1] == "N":
                prefix_n[i] += 1
        
        for i in range(n - 1, -1, -1):
            postfix_y[i] = postfix_y[i + 1]
            if customers[i] == "Y":
                postfix_y[i] += 1
        
        for i in range(n + 1):
            cur_penalty = prefix_n[i] + postfix_y[i]

            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                min_penalty_idx = i
        
        return min_penalty_idx