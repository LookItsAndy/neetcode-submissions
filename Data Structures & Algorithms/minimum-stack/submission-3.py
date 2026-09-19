class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []  # keep track of min values
        newMin = float('-inf')  # newMin remembers the global min value
    def push(self, val: int) -> None:
        # pushes elements to the top of the stack
        self.stack.append(val)
    
        if not self.minStack:   # if stack is empty, push first element into minStack
            self.minStack.append(val)
        else:
            newMin = min(val, self.minStack[-1])
            self.minStack.append(newMin)
    def pop(self) -> None:
        # removes the element form the top of the stack
        self.stack.pop()
        self.minStack.pop()
        
        

        
    def top(self) -> int:
        # returns the top element of the stack
        return self.stack[len(self.stack) - 1]
        
    def getMin(self) -> int:
        # returns the minimum element in the stack
        return self.minStack[-1]