class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # brute force approach: use a nested for loop and sliding window for each num in nums. on each num in nums, create small window, then increase while tracking the min length of a subwindow. Do this for every number in nums. This is O(n^2) because you use sliding window each time starting at nums[i] and going to the end.



        # optimized approach, use sliding window but use prefix to keep the sum of all elements in the window
        # if the current sum is less than the desired target, we can add one more element by expanding window to the left. This works because array contains all positive integers
        # if the current sum is equal to the desired target, do right - left + 1 to find a candidate for min

        if nums[0] >= target:   # check if first num is target, then return 1 since shortest subarr
            return 1

        minLength = float("inf")    # must be infinity since we dont know how big our data sets will be 

        left, right = 0, 1

        window_sum = nums[left] + nums[right]

        # target = 10
        # nums [2,1,5,1,5,3]
        # winsum = 9
        # left = 3  right = 5
        # minLength = inf

        while right < len(nums):
            
            if window_sum >= target:
                minLength = min(minLength, right - left + 1)
                window_sum -= nums[left]
                left+=1
            else:
                if right == len(nums) - 1:
                    break
                right += 1
                window_sum += nums[right]

      

        return minLength if minLength != float("inf") else 0