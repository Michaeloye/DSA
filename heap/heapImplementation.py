class Heap:
  def __init__(self):
    self.heap = []
    self.size = 0
  
  def insert(self, value):
    self.heap.append(value)
    self.size += 1

    self.heapify_up(self.size - 1)

  def extract_min(self):
    # swap root and last
    last = self.size - 1
    self.heap[0], self.heap[last] =  self.heap[last], self.heap[0]
    min_val = self.heap.pop()
    self.size -= 1

    self.heapify_down(0)
    return min_val

  def peek(self):
    return self.heap[0]

  def heapify_up(self, index):
    # calc parent
    parent_idx = (index - 1) // 2
    if index and self.heap[parent_idx] > self.heap[index]:
      # swap
      self.heap[parent_idx], self.heap[index] =  self.heap[index], self.heap[parent_idx]

      left = (parent_idx * 2) + 1
      right = (parent_idx * 2) + 2
      # if right in bound
      if right < self.size and self.heap[right] < self.heap[left]:
        # swap
        self.heap[left], self.heap[right] =  self.heap[right], self.heap[left]
      self.heapify_up(parent_idx)
  def heapify_down(self, index):
    left = (index * 2) + 1

    if left < self.size and self.heap[left] < self.heap[index]:
      self.heap[left], self.heap[index] =  self.heap[index], self.heap[left]

      self.heapify_down(left)

  def __str__(self):
    return f"{self.heap}"
  
  def __repr__(self):
    return f"{self.heap}"

