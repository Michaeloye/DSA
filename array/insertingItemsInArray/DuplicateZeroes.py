class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if not (any(elem == 0 for elem in arr)):
            arr
            return

        def moveArrayItems(array, start):
            res = array[start:]
            for idx, item in enumerate(array[start:]):
                rev_idx = len(res) - idx - 1

                if (rev_idx == len(res) - 1):
                    res[rev_idx] = 0
                else:
                    res[rev_idx + 1] = res[rev_idx]
                    res[rev_idx] = 0

            res = array[:start] + res
            return res

        _arr = arr
        # loop array
        # if we spot a zero move the next items by one step
        # add zero to the next postion

        i = 0
        for idx, item in enumerate(arr):
            if item == 0:
                _arr = moveArrayItems(_arr, idx + i)
                i += 1

        print(_arr)

        del arr[0:]
        arr += _arr
