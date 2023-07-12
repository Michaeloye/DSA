class Solution(object):
  def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    numOfOnes = 0
    numOfConsecutiveOnes = []
    maxNumOfConsecutiveOnes = 0

    for idx, x in enumerate(nums):
      if x == 1:
          numOfOnes += 1

      if x == 0 or (idx == len(nums) - 1):
        numOfConsecutiveOnes.append(numOfOnes)
        numOfOnes = 0
    
    for i in numOfConsecutiveOnes:
      if i > maxNumOfConsecutiveOnes:
        maxNumOfConsecutiveOnes = i

    return maxNumOfConsecutiveOnes