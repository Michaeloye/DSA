# https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        ans = []
        subStr = ""
        for i in range(len(s)):
            subStrSet = set(subStr)
            if s[i] in subStrSet:
                ans.append(subStr)
                subStr = s[i]
            else:
                subStr += s[i]

        # add last sub string after loop ends
        ans.append(subStr)

        return len(ans)
