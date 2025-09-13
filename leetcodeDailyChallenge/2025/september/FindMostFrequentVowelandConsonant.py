# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

class Solution:
    def maxFreqSum(self, s: str) -> int:
        VOWELS = set(['a', 'e', 'i', 'o', 'u'])
        vowels_map = {'-1': 0}
        consonants_map = {'-1': 0}

        for c in s:
            if c in VOWELS:
                vowels_map[c] = vowels_map.get(c, 0) + 1
            else:
                consonants_map[c] = consonants_map.get(c, 0) + 1
        
        vow_max_freq = max(vowels_map.values())
        con_max_freq = max(consonants_map.values())

        return vow_max_freq + con_max_freq