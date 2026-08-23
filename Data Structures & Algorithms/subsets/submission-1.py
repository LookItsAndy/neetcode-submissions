class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        #acm Solution
        
        result = []
        path = []
        # where am i allowed to pick from next
        def backtrack(start):
        # base case
            result.append(path[:])
        # call ourselves given some condition
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        #start index 0
        backtrack(0)
        return result