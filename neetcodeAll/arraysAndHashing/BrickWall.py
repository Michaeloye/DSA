# https://leetcode.com/problems/brick-wall/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        maxNum = len(max(wall, key=len))
        rowsWithMaxBricks = {}

        seenThresholds = set()

        for idx, row in enumerate(wall):
            if len(row) == maxNum:
                rowsWithMaxBricks[idx] = (row)
            else:
                wall[idx] = row + ((maxNum - len(row)) * [0])

        passThroughCount = len(wall)
        print(wall)
        for mRow in wall:
            i = 0
            threshold = mRow[i]
            while i < maxNum - 1:
                print("thresh", threshold)
                count = 0
                if threshold in seenThresholds:
                    i += 1
                    threshold += mRow[i]
                    continue
                for oRow in wall:
                    widthSum = 0
                    for width in oRow:
                        widthSum += width
                        if widthSum == threshold:
                            break
                        if widthSum > threshold:
                            count += 1
                            break

                    # if sum(oRow[0 : i + 1]) > threshold:
                    #     count += 1

                i += 1
                seenThresholds.add(threshold)
                print(passThroughCount, count)
                if mRow[i] == 0:
                    break
                threshold += mRow[i]
                passThroughCount = min(passThroughCount, count)

        return passThroughCount


# OPTIMIZED SOLUTION
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gapMap = {}
        maxGap = 0

        for row in wall:
            threshold = 0
            for brick in row[:-1]:
                threshold += brick
                if threshold in gapMap:
                    gapMap[threshold] += 1
                else:
                    gapMap[threshold] = 1

                maxGap = max(maxGap, gapMap[threshold])

        return len(wall) - maxGap
