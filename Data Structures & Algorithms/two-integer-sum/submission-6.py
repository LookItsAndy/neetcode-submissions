class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousMap = {}



        for index, num in enumerate(nums):

            difference = target - num

            if difference in previousMap:
                return [previousMap[difference], index]
            
            previousMap[num] = index