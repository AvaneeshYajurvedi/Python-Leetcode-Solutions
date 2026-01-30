'''Given an integer, convert it to a Roman numeral.'''
class Solution:
    def intToRoman(self, num: int) -> str:
        Roman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        total=""
        for i in range(len(Roman)):
            while num>=Roman[i][0]:
                total += Roman[i][1]
                num=num-Roman[i][0]
        return total
