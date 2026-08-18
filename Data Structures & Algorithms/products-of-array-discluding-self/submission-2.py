class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two loops, one for prefix, and one for postfix


        # result array will always be the same size of nums
        result = [1] * len(nums)

        prefix = 1
        postfix = 1

        # prefix loop

        for i in range(len(nums)):
            result[i] = result[i] * prefix
            prefix = prefix * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]

        return result