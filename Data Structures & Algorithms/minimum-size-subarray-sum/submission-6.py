class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        minLength = float("inf")

        left = 0
        right = 0
        window_sum = nums[left]
        while right < len(nums):

            if window_sum >= target:
                minLength = min(minLength, right - left + 1)
                window_sum -= nums[left]
                left += 1
            else:
                if right == len(nums) - 1:
                    break
                right +=1
                window_sum += nums[right]

        return minLength if minLength != float("inf") else 0
