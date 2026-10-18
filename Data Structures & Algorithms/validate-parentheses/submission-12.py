from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # given string, - > stack

        # for the stack: pop
        # '])'
        # stack = [(
        # ']'


        # ([ ])

       #  stack = ([
    
       # if "(" check if closing is ")"
                # true, continue

    # '{'


        # {([[( )]])} 

        # ({}[)]

        stack = deque([])
        # test []
        for ch in s:
            if ch == "[" or ch == "(" or ch == "{":               
                stack.append(ch)        # stack = [ '[' ]
                print(stack)
            elif not stack:
                return False
            
            elif ( (ch == ")" and stack.pop() != "(") or 
            (ch == "]" and stack.pop() != "[") or 
            (ch == "}" and stack.pop() != "{")):
                return False
            
        
        return (len(list(stack)) == 0)
            



            
