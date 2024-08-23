# https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:

        def LCM(nums):
            greater = min(nums)
            
            while True:
                found = True
                for num in nums:
                    if greater % num != 0:
                        found = False
                
                if found:
                    lcm = greater
                    break
                greater += 1
            return lcm

        def HCF(num1, num2):
            if num1 < num2:
                smaller = num1 
            else:
                smaller = num2
            hcf = smaller
            for k in range(1, smaller+1):
                if (num1 % k == 0) and (num2 % k == 0):
                    hcf = k
            return hcf

        CONSTANTS = ['0','1','2','3','4','5','6','7','8','9']
        denominators = []
        numerators = []

        i = 0
        while i < len(expression):
            num = []
            num2 = []

            if expression[i] == "/":
                i += 1
                while i < len(expression):
                    if expression[i] == '+' or expression[i] == '-':
                        break
                    num.append(expression[i])
                    i += 1
                num = int("".join(num))
                denominators.append(num)

            if i < len(expression) and (expression[i] == "+" or expression[i] == "-" or expression[i] in CONSTANTS):
                while i < len(expression):
                    if expression[i] == '/':
                        break
                    num2.append(expression[i])
                    i += 1

                num2 = int("".join(num2))
                numerators.append(num2)
        
        lcm = LCM(denominators)
        topSum = 0

        for i in range(len(numerators)):
            topSum += (lcm // denominators[i] ) * numerators[i]
        
        hcf = HCF(abs(topSum), abs(lcm)) if topSum != 0 else 1
        
        topSum = topSum // hcf
        lcm = lcm // hcf

        if topSum == 0:
            return "0/1"

        return f"{topSum}/{lcm}"
