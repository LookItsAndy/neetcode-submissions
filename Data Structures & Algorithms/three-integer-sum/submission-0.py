class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort nums array to make it easier to find duplicates and have decreasing and increasing sum pointers

        # start by checking if the index before is a duplicate number then skip when past the first index
        # if no duplicate, make left and right pointers. left pointer is in front of current index and right pointer is last
        # while left is less than right, (left pointer should never pass right) check the 3 sum and adjust pointers accordingly
        # if 3 sum is greater than 0, right pointer needs to move down to smaller number
        # if 3 sum is less than 0, left pointer needs to move up to bigger number
        # if 3 sum is 0, append all three values, nums[i], nums[left], nums[right] to result
        # then move left pointer up one. but this could come across another duplicate value 
        # so make a while loop after moving left by 1 and check if nums[l] == nums[l-1] and l < r
        # return result

        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:

                threeSum = nums[i] + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1      # threeSum greater 0 so decrease right pointer
                elif threeSum < 0:
                    left += 1

                elif threeSum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result

