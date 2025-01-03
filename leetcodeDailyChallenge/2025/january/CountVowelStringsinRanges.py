# https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        VOWELS = set(["a", "e", "i", "o", "u"])

        prefixCount = [0] * (len(words) + 1)

        for i, w in enumerate(words):
            # check if valid word
            v = 0
            if w[0] in VOWELS and w[-1] in VOWELS:
                v += 1
            
            prefixCount[i + 1] = prefixCount[i] + v
        
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q

            ans[i] = prefixCount[r + 1] - prefixCount[l]

        return ans

