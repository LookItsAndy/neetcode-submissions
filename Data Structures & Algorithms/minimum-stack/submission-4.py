class MinStack:


    # intuition: have two arrays, the stack and the minStack. the important detail to accurately keep track of the min elements is to keep the length of the stack and minStack the same. each time a new value is pushed, compare to newMin which can either be the new value or the previous value. that way when ever you pop, it still remembers the old min because it was remembered through each time a new element is pushed.
    
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