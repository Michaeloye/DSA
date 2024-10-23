# https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score, reverse=True)
        positionMap = {}
        currPosition = 1
        topPositions = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}

        for num in sortedScore:
            positionMap[num] = topPositions[currPosition] if currPosition <= 3 else str(currPosition)
            currPosition += 1
        
        for i in range(len(score)):
            score[i] = positionMap[score[i]]


        return score