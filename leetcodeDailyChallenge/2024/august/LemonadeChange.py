# https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changeCount = defaultdict(int)

        for b in bills:
            if b == 10:
                if changeCount[5] >= 1:
                    changeCount[5] -= 1
                else:
                    return False
            if b == 20:
                if changeCount[10] >= 1 and changeCount[5] >= 1:
                    changeCount[10] -= 1
                    changeCount[5] -= 1
                elif changeCount[5] >= 3:
                    changeCount[5] -= 3
                else:
                    return False
            
            changeCount[b] += 1
        return True