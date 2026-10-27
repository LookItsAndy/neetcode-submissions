class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # approach: use a hashmap to find the reminder of sums as the key and value is index to verify if a subarray is at least 2. A good subarray is when a repeated remainder value is seen meaning there was a subarray that added a multiple of k, causing the remainder to repeat again.

        remainder = {0:-1}
        pre_sum = 0
        #fill hashmap
        for i in range(len(nums)):
            pre_sum += nums[i]
            r = pre_sum % k

            if r not in remainder:
                remainder[r] = i
            elif (i - remainder[r]) > 1:
                return True
        return False

        



        