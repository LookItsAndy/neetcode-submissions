class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # intuition: to find 3 numbers that equal to 0, we can iterate through entire array for a fixed number, then pick two pointers to see if there are any combiinations of numbers that are equal 0. this only works if we sort the entire list first


        result = []
        nums = sorted(nums)


        for i in range (len(nums)):

            if i > 0 and nums[i] == nums[i -1]:
                continue
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while (nums[left] == nums[left -1 ] and left< right ):
                        left += 1
                
                elif(sum > 0):      # if sum is greater than 0, move right pointers
                    right -= 1
                elif(sum < 0):      # if sum is less than 0, move left pointers
                    left += 1
                
        return result;
