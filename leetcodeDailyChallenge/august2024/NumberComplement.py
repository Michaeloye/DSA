# https://leetcode.com/problems/number-complement

class Solution:
    def findComplement(self, num: int) -> int:
        def decToBinary(number):
            rem = 0
            quotient = number
            res = []

            while quotient:
                rem = quotient % 2
                quotient = quotient // 2

                res.append(str(rem))

            return "".join(res[::-1])

        def binToDecimal(number):
            power = len(number) - 1
            q = deque(list(number))
            res = 0

            while q:
                num = q.popleft()
                res += int(num) * (2 ** power)
                power -= 1
            
            return res
        
        numInBin = decToBinary(num)
        numInBinComp = []

        for num in numInBin:
            if num == '1':
                numInBinComp.append('0')
            else:
                numInBinComp.append('1')
        
        numInBinComp = "".join(numInBinComp)

        return binToDecimal(numInBinComp)