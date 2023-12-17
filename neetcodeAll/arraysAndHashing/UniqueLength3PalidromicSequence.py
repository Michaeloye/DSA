# https://leetcode.com/problems/unique-length-3-palindromic-subsequences


# FIRST SOLUTION (time limit exceeded)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        numOfSeq = 0
        setOfSeq = set()

        for i in range(1, len(s)):
            left = set(s[0:i])
            right = set(s[i + 1:])
            for leftLetter in left:
                if leftLetter in right:
                    palindromeSubSeq = leftLetter + s[i] + leftLetter
                    if palindromeSubSeq in setOfSeq:
                        continue

                    setOfSeq.add(palindromeSubSeq)
                    numOfSeq += 1

        return numOfSeq

# SECOND SOLUTION O(26 * n)


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            if first[curr] == -1:
                first[curr] = i

            last[curr] = i

        ans = 0
        for i in range(26):
            if first[i] == -1:
                continue

            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])

            ans += len(between)

        return ans

# MOST OPTIMAL SOLUTION O(n)


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            ans += len(set(s[i+1: j]))
        return ans
