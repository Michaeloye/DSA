arr = [2, 2, 1, 4, 3, 7]

res = []


def combinationSum(idx, target, ds, ans):
    if target == 0:
        # to avoid actually appending a reference to the same list multiple times
        ans.append([*ds])
        return
    if target < 0:
        return
    if idx == len(arr):
        return

    curr = arr[idx]
    ds.append(curr)
    combinationSum(idx + 1, target - curr, ds, ans)

    ds.pop()
    combinationSum(idx + 1, target, ds, ans)


combinationSum(0, 7, [], res)

print(res)
