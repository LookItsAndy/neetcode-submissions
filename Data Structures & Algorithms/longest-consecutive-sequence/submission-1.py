class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)

        # if empty
        if not nums:
            return 0
        
        maxRun = 1  # defaut value 1
        # example: [2, 20, 4, 10, 3, 4, 5]

        # only start counting if num - 1 is not in hash
        for num in nums:
            # this indicates that it can be the first number in the sequence
            if not num - 1 in hash:
                run = 1
                while num + run in hash:
                    run += 1
                    maxRun = max(maxRun, run)

            
        return maxRun
