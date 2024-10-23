# https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def timeInMins(time):
            h, m = time.split(":")
            h = int(h) * 60
            m = int(m)

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

# USING BUCKET
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def timeInMins(time):
            h, m = time.split(":")
            h = int(h) * 60
            m = int(m)

            return h + m
        bucket = [False] * (60 * 24)
        minTime = 60 * 24
        maxTime = 0

        for time in timePoints:
            mins = timeInMins(time)

            if bucket[mins]:
                return 0
            bucket[mins] = True
            minTime = min(minTime, mins)
            maxTime = max(maxTime, mins)
        
        prev = minTime
        res = (60 * 24) - maxTime + minTime

        for time in range(prev + 1, maxTime + 1):
            if bucket[time]:
                diff = time - prev
                res = min(res, diff)
                prev = time

        return res
