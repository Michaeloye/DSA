# https://leetcode.com/problems/find-the-town-judge/description/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n < 2:
            return n

        trustMap = {} # [count, trustedBy]
        for i in range(len(trust)):
            a, b = trust[i]

            if a in trustMap:
                prevCount, trustedBy = trustMap[a]
                trustMap[a] = [prevCount + 1, trustedBy]
            else:
                trustMap[a] = [1, 0]

            if b in trustMap:
                prevCount, trustedBy = trustMap[b]
                trustMap[b] = [prevCount, trustedBy + 1]
            else:
                trustMap[b] = [0, 1]
        
        print(trustMap)
        for key in trustMap:
            count, trustedBy = trustMap[key]
            if count == 0 and trustedBy == n - 1:
                return key

        return -1