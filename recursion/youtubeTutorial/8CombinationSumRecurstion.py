arr =[2,3,5]

res = []
cache = set()


def combinationSum(idx, target, ds, ans):
    if tuple(ds) in cache:
        return

    if target == 0:
        # to avoid actually appending a reference to the same list multiple times
        ans.append([*ds])
        cache.add(tuple(ds))
        print(cache)
        return
    if target < 0:
        return
    if idx == len(arr):
        return

    curr = arr[idx]
    ds.append(curr)
    combinationSum(idx, target - curr, ds, ans)

    combinationSum(idx + 1, target - curr, ds, ans)

    ds.pop()
    combinationSum(idx + 1, target, ds, ans)


combinationSum(0, 8 , [], res)

print(res)


# OPTIMAL CODE

candidates = [2,3,5]
def combinationSum(idx, target, ds, ans):
    if idx == len(candidates):
        return
    if target == 0:
        ans.append([*ds])
        return

    if candidates[idx] <= target:
        ds.append(candidates[idx])
        combinationSum(idx, target - candidates[idx], ds, ans)
        ds.pop()

    combinationSum(idx + 1, target, ds, ans)

