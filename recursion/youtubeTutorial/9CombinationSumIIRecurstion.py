candidates = [2, 2, 1, 4, 3, 7]

res = []


def combinationSum(idx, target, ds, ans):
    if target == 0:
        ans.append([*ds])
        return
    if idx == len(candidates):
        return

    for i in range(idx, len(candidates)):
        if i > idx and candidates[i] == candidates[i - 1]:
            continue
        
        if candidates[i] > target:
            break
        
        ds.append(candidates[i])
        combinationSum(i + 1, target - candidates[i], ds, ans)
        ds.pop()

candidates.sort()

combinationSum(0, 9, [], res)
print(res)