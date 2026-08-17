class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]


    # 1, 1 ,1 ,2,2,3
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, value in count.items():
            #value is the number of times num appeared
            freq[value].append(num)
        
        # set up for answer

        result = []

        # start at last index, end at 0, -1 means reverse
        for i in range(len(freq) - 1, 0 , -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result