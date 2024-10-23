# https://leetcode.com/problems/sort-the-people

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nameHeightMap = {}
        for i in range(len(heights)):
            nameHeightMap[heights[i]] = names[i]

        heights = sorted(heights, reverse = True)

        ans = []

        for height in heights:
            ans.append(nameHeightMap[height])
        
        return ans