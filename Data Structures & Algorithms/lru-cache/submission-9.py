class Node:
    def __init__(self,key:int,val:int):
        self.val = val
        self.key = key
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.leftDummy = Node(0,0)
        self.rightDummy = Node(0,0)
        self.leftDummy.right = self.rightDummy
        self.rightDummy.left = self.leftDummy
        self.hash_table = {}

    def get(self, key: int) -> int:
        if key in self.hash_table:
            self.remove(self.hash_table[key])
            self.insert(self.hash_table[key])
            return self.hash_table[key].val
        return -1
        
    def insert(self,node):
        left,right = self.rightDummy.left, self.rightDummy
        left.right = right.left =  node
        node.right = right
        node.left = left
    
    def remove(self,node):
        left,right = node.left,node.right
        left.right, right.left = right,left


    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            self.remove(self.hash_table[key])
        self.hash_table[key] = Node(key,value)
        self.insert(self.hash_table[key])

        if len(self.hash_table)>self.capacity:
            lru = self.leftDummy.right
            self.remove(lru)
            del self.hash_table[lru.key]

        
        

        
        
