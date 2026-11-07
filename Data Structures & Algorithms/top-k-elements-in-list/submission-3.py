class Solution(object):
   def topKFrequent(self, nums, k):
       """
       :type nums: List[int]
       :type k: int
       :rtype: List[int]
       """

       # heapq is a library
    #    heapq.heappush
    #    heapq.heappop
    #    heapq.heapify([1,2,2,2,212,1])

       counts = {}
       for num in nums:
           counts[num] = counts.get(num, 0) + 1



       top_k_heap = []
       # multiple keys can have the same value/count, reason why we need element and value
       for num in counts.keys():
           heapq.heappush(top_k_heap, (counts[num], num))


           if len(top_k_heap) > k:
               # remove everything from the heap?
               # does that mean we found all k elements?
               # remove something from heap
               heapq.heappop(top_k_heap)


       res = []
       for i in range(k):
           res.append(heapq.heappop(top_k_heap)[1])


       return res


      




             






               # if len of the heap is less then k, return all elements
               # this will not happen










      









