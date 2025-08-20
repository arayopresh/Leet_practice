class Solution:
    def isValid(self, s: str) -> bool:
    
        stack = []
            # using a dic to match the closing to opening bracks
        match = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in "([{":  # opening bracket
                stack.append(char)

            elif char in ")]}":  # closing brac
                if not stack:  # nun to match
                    return False

                elif stack[-1] == match[char]:  # if top element has a match
                    stack.pop()
                    #return True #will nstop after one valid pair is found

                else:
                    return False


        return not stack #for when the stack is empty
