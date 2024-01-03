# https://leetcode.com/problems/number-of-laser-beams-in-a-bank

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beamsCount = 0
        prev = 0
        for row in bank:
            numberOfSecurityDevices = row.count('1')

            if numberOfSecurityDevices != 0:
                beamsCount += numberOfSecurityDevices * prev

                prev = numberOfSecurityDevices

        return beamsCount
