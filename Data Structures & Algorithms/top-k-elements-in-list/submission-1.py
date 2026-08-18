class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]


        #build the hashtable for times a number appears where key -> integer value -> # times appeared
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            # key -> 7
            # value -> 2

        # use key and value from count to build freq list. where index represents amount of times integer appears. Max index is
        # always the length of the input array
        for key, value in count.items():
            freq[value].append(key)


        # freq -> [ [], [], [7], ]
        #            0   1   2 
        result = []
        # go through freq list in reverse order to find the top frequent numbers. check for k after appending to result
        for i in range(len(nums), 0, -1):
            # nums = [7,7] (start at i = 2)

            # go through each num inside each index
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
