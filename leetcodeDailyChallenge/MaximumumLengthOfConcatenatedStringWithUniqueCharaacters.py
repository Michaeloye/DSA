# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uniqueItemsLen = [0]

        def sq(idx, ds, unique):
            if idx >= len(arr):
                concatenatedStr = ""
                for item in ds:
                    concatenatedStr += item

                if len(concatenatedStr) == len(set(concatenatedStr)):
                    unique.append(len(concatenatedStr))

                return

            ds.append(arr[idx])
            idx += 1
            sq(idx, ds, unique)

            ds.pop()
            sq(idx, ds, unique)

        sq(0, [], uniqueItemsLen)
        return max(uniqueItemsLen)
