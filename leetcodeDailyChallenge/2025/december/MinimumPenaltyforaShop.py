# https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_n = [0] * (n + 1) # count Ns
        postfix_y = [0] * (n + 1) # count Ys
        min_sum = n + 1
        min_sum_idx = 0

        for l in range(1, n + 1):
            di = 1 if customers[l - 1] == 'N' else 0
            prefix_n[l] = prefix_n[l - 1] + di

        for r in range(n - 1, -1, -1):
            di = 1 if customers[r] == 'Y' else 0
            postfix_y[r] = postfix_y[r + 1] + di
        
        for i in range(n + 1):
            cur_sum = prefix_n[i] + postfix_y[i]

            if cur_sum < min_sum:
                min_sum = cur_sum
                min_sum_idx = i

        return min_sum_idx
