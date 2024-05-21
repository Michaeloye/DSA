# https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boatCount = 0
        l = 0
        r = len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                boatCount += 1
                l += 1
                r -= 1
            else:
                boatCount += 1
                r -= 1
        
        return boatCount