# https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXor = [0 for _ in range(len(arr) + 1)]
        ans = [0 for _ in range(len(queries))]

        for i in range(len(arr)):
            prefixXor[i + 1] = arr[i] ^ prefixXor[i]
        
        for i in range(len(queries)):
            l, r = queries[i]

            ans[i] = prefixXor[r + 1] ^ prefixXor[l]

        return ans