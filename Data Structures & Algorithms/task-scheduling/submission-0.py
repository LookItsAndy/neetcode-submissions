from collections import deque

class Solution(object):

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq_heap = []
        seen = {}
        time = 0
        q = deque() # hold list [-count, idletime]

        # loop to count all the tasks
        for task in tasks:
            seen[task] = seen.get(task, 0) + 1

        # push tasks into heap and sort

        for task in seen:
            heapq.heappush(freq_heap, (-1)*seen[task])
            heapq.heapify(freq_heap)


        while q or freq_heap:
            time += 1

            if freq_heap:
                count = 1 + heapq.heappop(freq_heap)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(freq_heap, q.popleft()[0])
        return time


        
        # after we have all the values in the heap, we want to get the first value that appears the most time, i think its easier to pop if this value is at the bottom so we need a minHeap instead of a maxheap. multiple every count in heap by (-1)


       # a counter for freq
       # a heap to sort these counts?


       # order
       # if we put all tasks in a heap?
       # we dont have order info


       # a good way to maintain order?
       # stacks and queue?
       # lifo and fifo
       # ordering? what is better ->


    #    imagine we use a stack


    #    a b c d
    #    d will arrive last
    #    d will go out first?


    #    how will d go out first?


    #    queue? a comes in and a goes out
    #    b -> b


    #    # we use a queue to order things
    #    # queue = (task, time)?
    #    # time = 0?
    #    time will determine the cool off period


    #    time + n to account for cool off and then keep doing that task every n times till we have nothing left
        





