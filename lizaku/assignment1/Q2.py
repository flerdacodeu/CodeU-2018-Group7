import random

class LinkedList:
    def __init__(self):
        self.head = None
    
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next 
    
    def append(self, val):
        new_node = self.Node(val, self.head)
        self.head = new_node

def find_kth_from_end(node, k):
    # returns None if the list is empty or the kth element from end does not exist
    # (15 from the end if the list has 10 elements)
    if node is None: # list has ended
        return (0, None) 
    (pos, val) = find_kth_from_end(node.next, k) # return the value and the position of the node
    if pos == k: # is it the position that we look for?
        val = node.val
    pos += 1
    return (pos, val)
        
l = LinkedList()
for i in range(10):
    l.append(random.randint(0,20))

print('kth from the last element is', find_kth_from_end(l.head, 1)[1])
