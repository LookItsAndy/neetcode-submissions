class Solution:
    def isValid(self, s: str) -> bool:

        #intuition: an opening bracket must be followed by a closing bracket. this is true as long as each pair is removed 
        # from inside to outside. ex: [({})] the {} pair will be removed then string will become [()] and so on. 
        # This can be accomplished by having two differnt logics. 
        # One for when we see a closing bracket: 
        # 1. check if bracket is inside close bracket hashmap
        # 2. check if stack is empty and also check if the last value inside the stack matches to the closing bracket (key) : value
        # 3. if yes, use pop() on the stack. if no, return false because the opening bracket does not match the closing bracket

        # Second logic, if open bracket is seen:
        # append the opening bracket to the stack to be popped later.


        stack = []  # add opening brackets to the stack
        closeToOpen = {
            ")" : "(", 
            "]" : "[", 
            "}" : "{"
            }

        for ch in s:
            if ch in closeToOpen:
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False     # interpretation: return true if stack is NOT full else make false. if stack is not empty, string is not valid