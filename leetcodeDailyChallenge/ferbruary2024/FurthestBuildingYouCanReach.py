class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxDiffs = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff <= 0:
                continue
            
            bricks -= diff
            maxDiffs.append(diff)

            if bricks < 0:
                if ladders == 0:
                    return i

                maxDiff = max(maxDiffs)
                maxDiffs.pop(maxDiffs.index(maxDiff))
                bricks -= maxDiff
                ladders -= 1

        return len(heights) - 1
