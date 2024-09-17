# https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordsCount = {}
        words1 = s1.split(" ")
        words2 = s2.split(" ")
        ans = []

        for w1 in words1:
            wordsCount[w1] = 1 + wordsCount.get(w1, 0)

        for w2 in words2:
            wordsCount[w2] = 1 + wordsCount.get(w2, 0)

        for w in wordsCount:
            if wordsCount[w] == 1:
                ans.append(w)
        return ans


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordSet = set()
        ans = set()
        words1 = s1.split(" ")
        words2 = s2.split(" ")

        for w1 in words1:
            if w1 not in wordSet:
                ans.add(w1)
            elif w1 in wordSet and w1 in ans:
                ans.remove(w1)
            wordSet.add(w1)

        for w2 in words2:
            if w2 not in wordSet:
                ans.add(w2)
            elif w2 in wordSet and w2 in ans:
                ans.remove(w2)
            wordSet.add(w2)

        return list(ans)
