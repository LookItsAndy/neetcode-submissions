class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        # differentiate between a number and a operand
        stack = []
        # [2, 1]
        # [3,3]
        # [9]
        for i in range(len(tokens)):
            if tokens[i] not in operators:      
                stack.append(int(tokens[i]))
            elif (tokens[i] == "+"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+ num2)

            elif (tokens[i] == "-"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)

            elif (tokens[i] == "*"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)

            elif (tokens[i] == "/"):
                num1 = stack.pop()
                num2 = stack.pop()
               
                stack.append(int(num2 / num1))
            

        return stack[0]