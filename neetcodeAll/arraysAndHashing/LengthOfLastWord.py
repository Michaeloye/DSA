# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in s[::-1]:
            if i != " ":
                count += 1
            if i == " " and count:
                return count

        return count
