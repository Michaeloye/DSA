# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleast(k):
            vowels = "aeiou"
            l = 0
            ans = 0
            vowelCount = {}
            consonantCount = 0

            for r in range(len(word)):
                if word[r] in vowels:
                    vowelCount[word[r]] = 1 + vowelCount.get(word[r], 0)
                else:
                    consonantCount += 1
                
                while len(vowelCount) == 5 and consonantCount >= k:
                    ans += len(word) - r

                    if word[l] in vowels:
                        vowelCount[word[l]] -= 1
                        if vowelCount[word[l]] == 0:
                            vowelCount.pop(word[l])
                    else:
                        consonantCount -= 1
                    l += 1
            return ans
        
        return atleast(k) - atleast(k + 1)