class Solution:
    def frequencySort(self, s: str) -> str:
        freqMap = {}
        reverseMap = {}
        ans = []
        
        for letter in s:
            freqMap[letter] = 1 + freqMap.get(letter, 0)
            
        sortedValues = sorted(freqMap.values(), reverse=True)
        
        for key in freqMap:
            val = freqMap[key]
            
            if val in reverseMap:
                reverseMap[val].append(key)
            else:
                reverseMap[val] = [key]

        
        for freq in sortedValues:

            while reverseMap[freq]:
                letter = reverseMap[freq].pop()
                for i in range(freq):
                    ans.append(letter)

        return "".join(ans)