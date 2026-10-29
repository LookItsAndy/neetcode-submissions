class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # brute force: nested for loop for sliding window


        for i in range (len(nums)):
            prefix = nums[i]
            for j in range(len(nums)):
                if i + j + 1 == len(nums):
                    break
                prefix += nums[i + j + 1]

                if prefix % k == 0:
                    return True
        
        return False