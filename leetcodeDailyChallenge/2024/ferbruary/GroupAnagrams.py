# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {} # str -> andIdx
        ans = []
        i = 0

        while i < len(strs):
            sortedStr = ''.join(sorted(strs[i]))

            if sortedStr in wordMap:
                position = wordMap[sortedStr]
                ans[position].append(strs[i])
            else:
                wordMap[sortedStr] = len(ans)
                ans.append([strs[i]])

            i += 1

        return ans