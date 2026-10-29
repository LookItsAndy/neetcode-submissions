class Node:

    # double linked list implementation
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}     # map key to the Node


        # dummy nodes
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left


    # helper functions
    
    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at the right most position of linked list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    
    def get(self, key: int) -> int:
        # everytime we get a value, we need to update it to the most recent
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        # if key already exists
        if key in self.cache:
            self.remove(self.cache[key])
        
        # else make new new with key, val

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:      # if cache is full, we need to remove the LRU node and remove from linked list

            lru = self.left.next    # left pointer is the least recently used
            self.remove(lru)
            self.cache[lru.key]
            del self.cache[lru.key]




        
