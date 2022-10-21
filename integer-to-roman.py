class Solution(object):
    def findLargestFitIndexUpTo(self, num, validValues, index):
        i = index
        
        while (num < validValues[i]):
            i -= 1
        return i
    
    def findLargestFitIndex(self, num, validValues):
        return self.findLargestFitIndexUpTo(num, validValues, len(validValues) - 1)
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        lookup = {1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL", 50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
        validValues = tuple(lookup.keys())
        li = self.buildListOfStrings(num, validValues, lookup)
        # print("".join(li))
        return "".join(li)

    def buildListOfStrings(self, num, validValues, lookup):
        n = num
        li = []
        i = len(validValues) - 1
        while (n > 0):
            i = self.findLargestFitIndexUpTo(n, validValues, i)
            val = validValues[i]
            li.append(lookup[val])
            n -= val
        return li