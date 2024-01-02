# https://leetcode.com/problems/push-dominoes/

from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        length = len(dominoes)
        lastSeenLetter = ""
        lastSeenLettterIdx = 0

        finalString = ""

        for i in range(length):
            if dominoes[i] != '.':
                finalString += dominoes[i]
                lastSeenLetter = dominoes[i]
                lastSeenLettterIdx = i

            else:
                rightLetter = "."
                idx = 0
                if i + 1 < length:
                    for j in range(i + 1, length):
                        if dominoes[j] == 'L' or dominoes[j] == 'R':
                            rightLetter = dominoes[j]
                            idx = j
                            break

                    if rightLetter == "L":
                        if lastSeenLetter == "R":
                            if (i - lastSeenLettterIdx) - (idx - i) == 0:
                                finalString += '.'
                            elif (i - lastSeenLettterIdx) > (idx - i):
                                finalString += 'L'
                            else:
                                finalString += 'R'
                        else:
                            finalString += 'L'

                    else:
                        if lastSeenLetter == 'R':
                            finalString += 'R'
                        else:
                            finalString += '.'

                else:
                    if lastSeenLetter == 'R':
                        finalString += 'R'
                    else:
                        finalString += '.'

        return finalString

soln = Solution()
print(soln.pushDominoes("R.R.L"))

# SOLUTION 2

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        letters = list(dominoes)
        queue = deque()

        for i, lett in enumerate(dominoes):
            if lett != '.':
                queue.append((i, lett))

        while queue:
            i, lett = queue.popleft()

            if lett == 'L':
                if i > 0:
                    if letters[i-1] == '.':
                        queue.append((i - 1, 'L'))
                        letters[i-1] = 'L'
            elif lett == 'R':
                if i + 1 < len(letters) and letters[i + 1] == '.':
                    if i + 2 < len(letters) and letters[i + 2] == 'L':
                        queue.popleft()
                    else:
                        letters[i + 1] = 'R'
        return ''.join(letters)

