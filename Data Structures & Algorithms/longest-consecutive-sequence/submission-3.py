class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force: sorting, check for consecutive sequences 
        
        # another brute force:
        # make set with nums, for each index, look up if the element + 1 is inside the set and keep going while counting until no more. 
        # time - O(n^2) because outter loop and inner loop
        # space - O(n)





        # optimized solution: 
        # hashset: find the beginning of a sequence and start counting
        # avoids repetitive actions



        hashset = set(nums)
        maxRuns = 0


        for i in range(len(nums)):
            runs = 0
            if nums[i]-1 not in hashset:
                # beginning of a sequence
                runs += 1
                while nums[i] + runs in hashset:
                    runs += 1
                    # track all sequences
                # after, save runs
                maxRuns = max(maxRuns, runs)
        
        return maxRuns
            

