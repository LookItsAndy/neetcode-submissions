class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        # make default stack filled with 0


        for index, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:   # last pair and first element (temp)

                stackTemp, stackIndex = stack.pop()
                # save stackTemp and stackIndex
                
                result[stackIndex] = (index - stackIndex)

            stack.append([temp, index])

        return result



