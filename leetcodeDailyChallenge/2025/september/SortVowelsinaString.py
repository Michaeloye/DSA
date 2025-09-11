# https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution:
    def sortVowels(self, s: str) -> str:
        # go through the string s, for every vowel you see add to the vowels
        # array
        # sort the vowels array
        # go through the string s, replace each vowel, with the i the position 
        # vowel
        # return string

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        n = len(s)

        seen_vowels = []

        for c in s:
            if c in vowels:
                seen_vowels.append(c)
        seen_vowels.sort()

        j = 0 # new position of vowel
        for i in range(n):
            if s[i] in vowels:
                s[i] = seen_vowels[j]
                j += 1

        return "".join(s)
