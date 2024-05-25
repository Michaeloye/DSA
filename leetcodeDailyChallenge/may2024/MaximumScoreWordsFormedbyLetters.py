# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def letterAvailable(w, lettersCnt):
            lCnt = Counter(w)

            for c in lCnt:
                if lCnt[c] > lettersCnt[c]:
                    return False
            return True

        lettersCnt = Counter(letters)

        def getScore(w):
            res = 0

            for c in w:
                res += score[ord(c) - ord('a')]
            return res
        def dfs(i):
            if i == len(words):
                return 0
            
            # don't pick
            res = dfs(i + 1)

            # pick
            if letterAvailable(words[i], lettersCnt):
                for c in words[i]:
                    lettersCnt[c] -= 1

                res = max(res, getScore(words[i]) + dfs(i + 1))

                for c in words[i]:
                    lettersCnt[c] += 1
            return res
        
        return dfs(0)