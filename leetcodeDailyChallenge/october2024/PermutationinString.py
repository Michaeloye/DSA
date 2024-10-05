# https://leetcode.com/problems/permutation-in-string/

# O(26 * n)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = Counter(s1)
        s2Map = {}
        r = len(s1) - 1

        for i in range(len(s1)):
            letter = s2[i]
            s2Map[letter] = 1 + s2Map.get(letter, 0)

        l = 0
        while r < len(s2):
            if s1Map == s2Map:
                return True

            s2Map[s2[l]] -= 1
            if s2Map[s2[l]] == 0:
                s2Map.pop(s2[l])
                
            l += 1
            r += 1
            if r < len(s2):
                s2Map[s2[r]] = 1 + s2Map.get(s2[r], 0)

        return False


# O(n) solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Map = {}
        s2Map = {}

        for i in range(26):
            char = chr(i + ord('a'))
            s1Map[char] = 0
            s2Map[char] = 0

        for i in range(len(s1)):
            letter1 = s1[i]
            s1Map[letter1] += 1
            letter2 = s2[i]
            s2Map[letter2] += 1
        
        matches = 0
        # check matches
        for i in range(26):
            letter = chr(i + ord('a'))
            if s1Map[letter] == s2Map[letter]:
                matches += 1

        l = 0
        
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            s2Map[s2[r]] += 1
            if s1Map[s2[r]] == s2Map[s2[r]]:
                matches += 1
            elif s1Map[s2[r]] + 1 == s2Map[s2[r]]:
                matches -= 1

            s2Map[s2[l]] -= 1

            if s1Map[s2[l]] == s2Map[s2[l]]:
                matches += 1
            elif s1Map[s2[l]] - 1 == s2Map[s2[l]]:
                matches -= 1

            l += 1

        return matches == 26
