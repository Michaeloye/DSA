# def duplicateZeros(arr):
#         _arr = arr
#         # loop array
#         # if we spot a zero move the next items by one step
#         # add zero to the next postion

#         i = 0
#         for idx, item in enumerate(arr):
#             print(_arr)
#             if item == 0:
#                 print (idx)
#                 _arr = moveArrayItems(_arr, idx + i)
#                 i += 1
#         return _arr

# def moveArrayItems(array, start):
#         res = array[start:]
#         for idx, item in enumerate(array[start:]):
#             rev_idx = len(res) - idx - 1

#             if (rev_idx == len(res) - 1):
#                 res[rev_idx] = 0
#             else:
#                 res[rev_idx + 1] = res[rev_idx]
#                 res[rev_idx] = 0

#         res = array[:start] + res
#         return res
def duplicateZeros(arr) -> None:
    """
        Do not return anything, modify arr in-place instead.
        """
    n = len(arr)
    queue = []
    for i in range(n):
        queue.append(arr[i])
        if arr[i] == 0:
            print("ZERO")
            queue.append(0)
        arr[i] = queue.pop(0)
        print(queue)
        print(arr)


a = [0, 1, 3, 2, 5, 0]
duplicateZeros(a)
100300
