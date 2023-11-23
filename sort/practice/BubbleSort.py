from random import randint

def bubbleSort(array):
  wasSwapped = False
  i = 0

  while True:
    if i < len(array) - 1:
      if array[i + 1] < array[i]:
        array[i], array[i + 1] = array[i + 1], array[i]
        wasSwapped = True
      i += 1

    else:
      if not wasSwapped:
        break
      wasSwapped = False
      i = 0

  return array

a = [randint(0, i) for i in range(100)]
print(bubbleSort(a))