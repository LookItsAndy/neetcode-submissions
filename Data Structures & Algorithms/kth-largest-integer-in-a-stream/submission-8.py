class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:   # maintain consistent heap length
            heapq.heappop(self.min_heap)
        
        if nums:                # if the list is empty, we dont want to fill heap because there are no numbers to use yet
            while len(self.min_heap) < k:
                heapq.heappush(self.min_heap, self.min_heap[0])
        print(self.min_heap)
        

    def add(self, val: int) -> int:

        if self.min_heap:

            heapq.heappush(self.min_heap, val)
        # if len(self.max_heap) > self.k:  # pop because we only want k values inside heap
        # no condidtion because we already trim down the size of heap in constructor
        # just need to add one, and remove one

            heapq.heappop(self.min_heap)
        else:
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0] 


