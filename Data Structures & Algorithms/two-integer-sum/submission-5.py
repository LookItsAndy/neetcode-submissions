class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        # intuition: finding two sum is possible through a one pass hash map. While iterating through the nums array,
        # we calculate the differnce of the target and current value. This gives a possible answer that we use to search the current
        # hashmap. Since every sum has two solutions, this will work once we get to the second valid value which is always 
        # through the one pass. 
        # 1. find difference. 
        # 2. check if answer is contained in hashmap yet. 
        # 3. if true, return the two indexes where the value is present. 
        # 4. if false, add to hashmap and continue iterating


        prevMap = {}    #key -> value : value -> index

        for i, n in enumerate(nums):    # enumerate gives index and value same time
            difference = target - n

            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[n] = i

        