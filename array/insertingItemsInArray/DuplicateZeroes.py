class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # queue is first in first out
        queue = []

        # so loop through the arr, append items in arr to queue, if 0 append 0 again, lastly pop(0) from queue to arr[index]
        for i in range(len(arr)):
            queue.append(arr[i])
            if arr[i] == 0:
                queue.append(0)

            arr[i] = queue.pop(0)
