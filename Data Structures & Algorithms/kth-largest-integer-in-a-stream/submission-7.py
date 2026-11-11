class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = nums
        heapq.heapify(self.max_heap)

        while len(self.max_heap) > k:   # maintain consistent heap length
            heapq.heappop(self.max_heap)
        
        if nums:
            while len(self.max_heap) < k:
                heapq.heappush(self.max_heap, self.max_heap[0])
        print(self.max_heap)
        

    def add(self, val: int) -> int:

        if self.max_heap:

            heapq.heappush(self.max_heap, val)
        # if len(self.max_heap) > self.k:  # pop because we only want k values inside heap
        # no condidtion because we already trim down the size of heap in constructor
        # just need to add one, and remove one

            heapq.heappop(self.max_heap)
        else:
            heapq.heappush(self.max_heap, val)

        return self.max_heap[0] 


