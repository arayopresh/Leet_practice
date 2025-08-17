class Solution:
    def isPalindrome(self, x: int) -> bool:


        x =str(x) #typecating the int into a string

        reversed = x[::-1] #reverse using string slicing

        if reversed == x:
            return True #using return bc just having a true wont show the value so the output is none rather than T/F
        else:
            return False



    #converting a string first then reversing the string and comparing


    
        