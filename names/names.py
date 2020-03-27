import sys
sys.path.append('../ring_buffer')
from doubly_linked_list import DoublyLinkedList
import time



start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
'''
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

Nested for loop:

64 duplicates
runtime: 4.412265777587891 seconds

for every name in names1 we iterate through the entire names2
list. bad bad bad
'''

# Let's use an LRU cache

# class LRUCache:

#     def __init__(self, limit=10):
#         self.limit = limit
#         self.lis = DoublyLinkedList()
#         self.size = 0
#         self.cache = {}


#     def get(self, key):
#         if key in self.cache:
#             out = self.cache[key]
#             self.lis.move_to_front(out)
#             return out.value[1]
#         else:
#             return None

#     def set(self, key, value):
#         if key in self.cache:
#             inp = self.cache[key]
#             inp.value = (key, value)
#             self.lis.move_to_front(inp)
#             return inp
        
#         if self.size is self.limit:
#             self.cache.pop(self.lis.remove_from_tail()[0])
#             self.size -=1
#         self.lis.add_to_head((key, value))
#         self.cache[key] = self.lis.head
#         self.size += 1

# # Create instance of LRUCache with limit 10,000 (len(names))
# lru = LRUCache(10000)

# for i in names_1:
#     lru.set(i, i)

# for i in names_2:
#     if lru.get(i) == i:
#         duplicates.append(i)

# '''
# LRUCache: 

# 64 duplicates
# runtime: 0.02150416374206543 seconds
# Huge improvement
# '''


# Binary Search Tree

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

tree = BinarySearchTree(names_1[0])

for i in names_1:
    tree.insert(i)

for j in names_2:
    if tree.contains(j):
        duplicates.append(j)

'''
Binary Search Tree:

64 duplicates
runtime: 0.07851338386535645 seconds
'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# # First attempt, list comprehension
# [duplicates.append(i) for i in names_1 if i in names_2]

# '''
# List comp:

# 64 duplicates
# runtime: 0.8901548385620117 seconds

# Good improvement, could probably do better!
# '''