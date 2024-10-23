# https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        while count:
            n = min(count)

            for _ in range(groupSize):
                if n in count:
                    count[n] -= 1
                    if count[n] == 0:
                        count.pop(n)
                else:
                    return False
                n += 1
        return True
