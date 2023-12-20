# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences

class Solution:
    def maxProduct(self, s: str) -> int:
        length = len(s)
        paliMap = {}
        maxProd = 0

        # so this is what we want (e.g for s = "paper")
        # 0 0 0 0 0
        # 0 0 0 0 1
        # 0 0 0 1 0
        # 0 0 0 1 1
        # 0 0 1 0 0
        # 0 0 1 0 1
        # and so on...

        # this gives us all the subsequences of s
        for mask in range(1, 2 ** length):
            subSeq = ""

            # now to know where we are in the mask, we use the bitwise AND operator
            # 0 0 0 0 0
            # 0 0 0 0 1
            # 0 0 0 1 0
            # 0 0 1 0 0
            # 0 1 0 0 0

            # so basically shift the 1
            # this helps us know where we are in the mask thus knowing which character we are at

            # so if we have a mask of 0 0 0 1 1
            # we'll be comparing with 0 0 0 0 1
            # then 0 0 0 1 0
            # and we have a string of "paper"
            # we know we are at the 3rd and 4th character
            # so we add those characters to our subsequence
            for i in range(length):
                if mask & (2 ** i):
                    subSeq += s[i]

            if subSeq == subSeq[::-1]:
                paliMap[mask] = len(subSeq)

        for i in paliMap:
            for j in paliMap:
                if i & j == 0:  # disjoint
                    maxProd = max(maxProd, paliMap[i] * paliMap[j])

        return maxProd
