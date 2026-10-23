class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # brute force method: nested for loop
        # time complexity: O(n^2)

        # optimized solution: we use prefix, 

        prefix_sum = 0


        # nums = [1,7,3,6,5,6]
                # total = 28 - 6 - 11 = 11
        # prefix = 11

        # i = 0

        # nums = [2,1,-1]
                # total = 2 - 2 - 0 
        # prefix = 0
        # postfix = 0
        # i = 1

        # nums = [3,2,1]
                # total = 6 - 1 - 5 = 0
        # prefix = 5
        
        total = sum(nums)


        for i in range(len(nums)):
            
            if (total - nums[i] - prefix_sum) == prefix_sum:
                 return i

            prefix_sum += nums[i]
            
            
        return -1
