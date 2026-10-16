class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force solution: 3 loops, for each i num, you go through each j num, which goes through each k num, checking if all three equal 0
        # time - O(n^3)
        # space - O(n)



        # optimized solution: 
        # sort entire array, start loop at index i, use two pointer method, left pointer is to the right of i, right index is last num. compute the sum using all three numbers. if sum is greater than 0, right pointer needs to decrease. if sum is less than 0, left pointer needs to increase. 
        # when all three nums equal 0, add to subset in array called result


        result = []
        nums.sort()

        for i in range (len(nums)):
            # if loop goes into a range of positive numbers, otaining 0 becomes impossible
            # also check if duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1


            while left < right:
                sum = nums[i] + nums[right] + nums[left]

                if sum < 0:
                    left += 1
                elif sum > 0: 
                    right -= 1
                elif sum == 0:
                    result.append([nums[i], nums[right], nums[left]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result



