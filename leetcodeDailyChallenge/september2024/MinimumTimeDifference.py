# https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def timeInMins(time):
            h, m = time.split(":")
            h = int(h) * 60
            m = int(m)
            
            if h == 0 and m == 0:
                return 24 * 60

            return h + m
        
        timeMins = []
        ans = 1440

        for time in timePoints:
            timeMins.append(timeInMins(time))
        timeMins.sort()

        for i in range(len(timeMins) - 1):
            diff = timeMins[i + 1] - timeMins[i]
            ans = min(ans, diff)

        # Consider the circular difference between last and first element
        first = timeMins[0]
        last = 1440 - timeMins[-1]
        ans = min(ans, first + last)

        return ans
