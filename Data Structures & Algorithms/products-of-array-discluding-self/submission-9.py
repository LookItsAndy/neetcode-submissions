class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force solution: for every index in the array, inner loop through the array again and multiply itself by every other number. skip itself in the inner loop.

        # the brute force solution:
        # result = [1] * len(nums)
        # for i in range(len(nums)):
            
        #     for j in range(len(nums)):

        #         if i != j:
        #             result[i] *= nums[j]

        # return result



        # optimized solution: 2 pass, have prefix loop and postfix loop
        # for prefix loop, use prefix = 1 then for each index in nums array, multiply element by prefix, update prefix by multiplying itself by the curr element. then go next

        # prefix = 1, [1,2,4,6].  1 * prefix = 1, prefix *= nums[i] -> 2*prefix = 2, prefix *= nums[i] = 2


        result = [1] * len(nums)

        prefix = 1
        postfix = 1


        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]

        # postfix must go backwards
        for i in range(len(nums) - 1, -1 , -1):     # start at last index, stop at -1 , go in reverse
            result[i] *= postfix
            postfix *= nums[i]

        return result
            