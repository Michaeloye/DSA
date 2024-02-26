arr = [1,2,2]

def subsets(idx, ds, ans):
  print(ds)
  if idx == len(arr):
    return
  
  for i in range(idx, len(arr)):
    if i > idx and arr[i] == arr[i - 1]:
      continue

    ds.append(arr[i])
    subsets(i + 1, ds, ans)
    ds.pop()

res = []
subsets(0, [], res)
print(res)
