# https://leetcode.com/problems/determine-if-string-halves-are-alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count1 = 0
        count2 = 0

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i in range(len(s) // 2):
            j = len(s) // 2 + i

            if s[i] in vowels:
                count1 += 1
            if s[j] in vowels:
                count2 += 1

        return count1 == count2
