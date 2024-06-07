# https://leetcode.com/problems/replace-words

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictSet = set(dictionary)

        words = sentence.split(" ")
        newSentence = []

        for word in words:
            for i in range(1,len(word) + 1):
                if word[:i] in dictSet:
                    newSentence.append(word[:i])
                    break
                if i == len(word):
                    newSentence.append(word[:i])
        
        return " ".join(newSentence)