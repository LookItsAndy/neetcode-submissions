class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])

        output = [intervals[0]] # add the first interval to output

        for start, end in intervals[1:]:
            # check the end of last interval
            endLastInterval = output[-1][1]

            if start <= endLastInterval:
                output[-1][1] = max(end, endLastInterval)   # modify the last end interval if current start is smaller, make it the bigger value
            else:
                output.append([start, end])

        return output
        
