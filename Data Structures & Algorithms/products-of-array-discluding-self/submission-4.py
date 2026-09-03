class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        postfix = 1

        # two pass solution approach, using left of i and right of i products. no need for left and right array, just multiply to result to keep o(1) space.


        # compute everything to left loop from start

        for i in range (len(nums)):
            result[i] *= prefix
            prefix *= nums[i]


        # compute everything to right loop from end

        for i in range (len(nums) - 1, -1, -1): # start at len(nums) - 1 because 0 index starting
                                                # end at -1 to include 0
                                                # -1 to go backwards
            result[i] *= postfix
            postfix *= nums[i]

        return result