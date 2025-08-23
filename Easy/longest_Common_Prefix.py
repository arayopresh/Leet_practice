from typing import List #imported for error purposes

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        for x in range (len(strs[0])): #itersting thru every index
            for y in strs:
                if x == len(y) or y[x] != strs[0][x]: #adding the first part bc i wanna check if it is within bounds
                    return prefix
            prefix = prefix +strs[0][x]
        
        return prefix



    #git credentials