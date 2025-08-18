class Solution:
    def romanToInt(self, s: str) -> int:
       roman_num = {"I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
       total = 0

       for x in range(len(s) -1):
        if roman_num[s[x]] < roman_num[s[x+1]]:
            total = total - roman_num[s[x]] 
        else:
            total = total + roman_num[s[x]]
       return total + roman_num[s[-1]]
        
        









#from the first index, compare if the first index value is bigger or smaller than the +1, 
# if the first is bigger, add the first, if it is not then subtract it from the totls so far