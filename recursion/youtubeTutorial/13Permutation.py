array = [1, 2, 3]
res = []

def permutation(idx):
  if idx == len(array):
    res.append([*array])
    return

  for i in range(idx, len(array)):
    array[idx], array[i] = array[i], array[idx]

    permutation(idx + 1)

    array[i], array[idx] = array[idx], array[i]

permutation(0)

print(res)