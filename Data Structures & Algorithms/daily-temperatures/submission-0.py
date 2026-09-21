class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # neetcode Solution
        result = [0] * len(temperatures)

        stack = [] # pair: [temp, index]


        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:    # if stack has elements and the last pair in the stack has a temperature less than the current temp
                # pop stack
                stackTemp, stackIndex = stack.pop()    # elements in stack are pairs
                # when popping, it means that a warmer temperature was found so add to result
                result[stackIndex] = (i - stackIndex)
                
            stack.append([temp, i])

        return result
            