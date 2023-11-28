class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        refStr = 'balloon'
        textMap = {i: 0 for i in refStr}
        refMap = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        for i in text:
            if i in textMap:
                textMap[i] += 1

        noOfPoss = textMap['b'] // refMap['b']

        if noOfPoss == 0:
            return 0

        for i in textMap:
            if noOfPoss == 0:
                return 0

            if textMap[i] // refMap[i] < noOfPoss:
                noOfPoss = textMap[i] // refMap[i]

        return noOfPoss
