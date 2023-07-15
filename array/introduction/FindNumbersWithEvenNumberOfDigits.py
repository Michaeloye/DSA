class Solution(object):
  def findNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    evenCount = 0

    for i in nums:
      if (len(str(i)) % 2) == 0:
        evenCount += 1

    return evenCount