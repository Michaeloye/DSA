# https://leetcode.com/problems/insert-interval/description/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intersections = []
        indexes = []

        # get interval where intersections occured
        for i in range(len(intervals)):
            start, end = newInterval
            a, b = intervals[i]

            if start in range(a, b + 1) or a in range(start, end + 1) or b in range(start, end + 1) or end in range(a, b + 1):
                intersections.append([a, b])
                indexes.append(i)
        
        # handle when there is no intersection
        if len(intersections) == 0:
            start, end = newInterval
            a, _ = intervals[0] if len(intervals) else [-1, -1]

            if a < start:
                intervals.append(newInterval)
            else:
                intervals.insert(0, newInterval)

            intervals.sort()
            return intervals

        # handle when there is intersection
        a, _ = intersections[0]
        _, b = intersections[-1]
        start, end = newInterval
        newStart = a if a <= start else start
        newEnd = b if b >= end else end
        
        i = 0

        while i < len(intervals):
            a, b = intervals[i]
            if i not in indexes:
                res.append([a, b])
            elif i in indexes and indexes[0] == i:
                res.append([newStart, newEnd])
                i += len(indexes)
                continue
            i += 1
        return res

# optimized solution
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < newInterval[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > newInterval[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)

        return res