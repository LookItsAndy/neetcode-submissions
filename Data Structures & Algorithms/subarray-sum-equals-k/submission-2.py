class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
         
        sum_hash = {0:1}

        sub_sum = 0
        count = 0
        for i in range(len(nums)):
            sub_sum += nums[i]
            desired = sub_sum - k
            
            if desired in sum_hash:
                count += sum_hash[desired]    
            
            sum_hash[sub_sum] = sum_hash.get(sub_sum, 0) + 1
            
        return count
            

