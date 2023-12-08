
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = ""

        for str in strs:
            length = len(str)

            res += f"{length}#{str}"
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        res = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            i = j + 1
            j = i + length
            res.append(str[i:j])
            i = j
        return res


soln = Solution()

encoded = soln.encode(["the", "boy", "is", "good"])
decoded = soln.decode(encoded)
print(decoded)
