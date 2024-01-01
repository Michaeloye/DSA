# https://leetcode.com/problems/repeated-dna-sequences

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dnaMap = {}
        ans = []
        for i in range(len(s)):
            if i + 10 <= len(s):
                subStr = s[i:i + 10]
                if subStr in dnaMap:
                    count = dnaMap[subStr]
                    dnaMap[subStr] = count + 1
                    if count == 1:
                        ans.append(subStr)
                else:
                    dnaMap[s[i:i + 10]] = 1
            else:
                break
        return ans
