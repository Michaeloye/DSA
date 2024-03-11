array = [1, 2, 3]
res = []

def permutation(ds, chosen):
  if len(ds) == len(array):
    res.append([*ds])
    return

  for i in range(len(array)):
    if i not in chosen:
      ds.append(array[i])
      chosen.add(i)
      permutation(ds, chosen)
      chosen.remove(i)
      ds.pop()



permutation([], set())
print(res)