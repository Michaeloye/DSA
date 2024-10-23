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

# if boat does not have a limit of two
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boatCount = 0
        currSum = 0

        for i in range(len(people)):
            currSum += people[i]

            if currSum == limit:
                boatCount += 1
                currSum = 0
            elif currSum > limit:
                boatCount += 1
                currSum = people[i]
        
        if currSum > 0 and currSum <= limit:
            boatCount += 1

        return boatCount


