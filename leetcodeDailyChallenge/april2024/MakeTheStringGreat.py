# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        def handler(sArr):
            if len(sArr) <= 1:
                return sArr

            newStr = sArr[:]
            i = 0
            while i < len(newStr) - 1:  # Changed to a while loop for proper iteration
                if (newStr[i].islower() and newStr[i + 1].isupper()) or (newStr[i].isupper() and newStr[i + 1].islower()):
                    if newStr[i].lower() == newStr[i + 1].lower():
                        newStr.pop(i)
                        newStr.pop(i)
                        return handler(newStr) 
                    else:
                        i += 1  # Move to the next character if no removal is done
                else:
                    i += 1  # Move to the next character if no removal is done
            
            return newStr  # Return newStr if no modifications were made

        return "".join(handler(list(s)))
