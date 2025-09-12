# https://leetcode.com/problems/vowels-game-in-a-string/

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel_count = 0
        VOWELS = ["a", "e", "i", "o", "u"]

        for c in s:
            if c in VOWELS:
                vowel_count += 1

        if vowel_count == 0:
            return False

        return True
