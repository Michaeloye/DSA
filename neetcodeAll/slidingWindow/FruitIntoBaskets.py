# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        total = 0
        l = 0
        ans = 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[l]
                total -= 1
                count[f] -= 1

                if count[f] == 0:
                    count.pop(f)
                l += 1

            ans = max(ans, total)
            
        return ans
