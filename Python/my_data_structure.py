class Stack:
  def __init__(self):
    self.array = []
  
  def is_empty(self):
    if len(self.array) == 0:
      return True
    else:
      return False

  def peek(self):
    if self.is_empty():
      return None
    else:
      return self.array[0]
  
  def push(self, item):
    self.array.append(item)
  
  def pop(self):
    if self.is_empty():
      return None
    else:
      last_item = self.array[-1]
      self.array = self.array[:-1]
      return last_item
  
  def to_array(self):
    if self.is_empty():
      return []
    return [i for i in reversed(self.array)]



class Queue:
  def __init__(self, priority=False):
    self.array = []
    self.priority = priority
  
  def is_empty(self):
    if len(self.array) == 0:
      return True
    else:
      return False

  def peek(self):
    if self.is_empty():
      return None
    else:
      return self.array[0]
  
  def enqueue(self, item):
    if self.priority:
      for idx, pair in enumerate(reversed(self.array)):
        if pair[0] <= item[0]:
          pos = len(self.array) - idx
          self.array.insert(pos, item)
    else:
      self.array.append(item)
  
  def dequeue(self):
    first_item = self.array[0]
    self.array = self.array[1:]
    return first_item
  
  def to_array(self):
    return self.array



class LinkedListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList ():
  def __init__(self, value):
    self.head = LinkedListNode(value)

  def check_item(self, value):
    pass
  
  def add(self, value):
    new_node = LinkedListNode(value)
    current_node = self.head
    while current_node.next != None:
      current_node = current_node.next
    current_node.next = new_node
  
  def remove(self, value):
    pass
  
  def print(self):
    arr = []
    current_node = self.head
    while current_node != None:
      arr.append(current_node.value)
      current_node = current_node.next
    return arr



def Hash(item):
  if isinstance(item, int):
    return item**2 % 10
  return hash(item)

class HashTable:
  def __init__(self, table_size=100):
    self.table = [dict() for _ in range(table_size)]
  
  def _check_key(self, item):
    idx = Hash(item[0])
    keys = list(self.table[idx].keys())
    if item[0] in keys():
      return True
    return False
  
  def check_item(self, item):
    check_key = self._check_key(item)
    if check_key:
      idx = Hash(item[0])
      if item[1] in self.table[idx][item[0]]:
        return True
    return False
  
  def add(self, item):
    item_check = self.check_item(item)
    if item_check:
      print(f"{item} exists in the table")
    else:
      key_check = self._check_key(item)
      idx = Hash(item[0])
      if key_check:
        self.table[idx][item[0]].append(item[1])
      else:
        self.table[idx][item[0]] = item[1]     
  
  def remove(self, item):
    item_check = self.check_item(item)
    if item_check:
      idx = Hash(item[0])
      check_len = len(self.table[idx][item[0]])
      if check_len < 2:
        del self.table[idx][item[0]]
      else:
        self.table[idx][item[0]].pop(item[1])
    else:
      print(f"{item} does not exist.")
  
  def to_array(self):
    return self.table



class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.head = None
  
  def add_leaf(self, value):
    if self.head == None:
      self.head = TreeNode(value)
    else:
      pass



# class Heap:
#   def __init__(self, heap_type):
#     if heap_type == "max":
#       self.heap_func = lambda a, b : max(a, b)
#     elif heap_type == "min":
#       self.heap_func = lambda a, b : min(a, b)
#     else:
#       raise RuntimeError("No such heap type is available")
#     self.heap_array = []
  
#   def insert(self, item):
#     self.heap_array.append(item)
#     if len(self.heap_array) > 2:
#       idx = len(self.heap_array) - 1
#       while self.heap_array[idx] == self.heap_func(self.heap_array[idx], self.heap_array[idx // 2]):
#         if idx >= 1:
#           self.heap_array[idx], self.heap_array[idx // 2] = \
#             self.heap_array[idx // 2], self.heap_array[idx]
#           if idx // 2 > 1:
#             idx = idx // 2
#           else:
#             break
  
#   def _check_item(self, item):
#     for i in self.heap_array:
#       if i == item:
#         return True
#     return False
  
#   def remove(self, item):
#     check_item = self._check_item(item)
#     if check_item:
      
#       smallest = 
#       if len(self.heap_array) > 2:
        
#       else:
#         p = self.heap_array.index(item)
#         self.heap_array.pop(p)
#     else:
#       print(f"{item} does not exist.")
#       return


"""
Min Heap Implementation in Python
"""
class MinHeap:
  def __init__(self):
    """
    On this implementation the heap list is initialized with a value
    """
    self.heap_list = [0]
    self.current_size = 0

  def sift_up(self, i):
    """
    Moves the value up in the tree to maintain the heap property.
    """
    # While the element is not the root or the left element
    Stop = False
    while (i // 2 > 0) and Stop == False:
      # If the element is less than its parent swap the elements
      if self.heap_list[i] < self.heap_list[i // 2]:
          self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
      else:
          Stop = True
      # Move the index to the parent to keep the properties
      i = i // 2

  def insert(self, k):
    """
    Inserts a value into the heap
    """
    # Append the element to the heap
    self.heap_list.append(k)
    # Increase the size of the heap.
    self.current_size += 1
    # Move the element to its position from bottom to the top
    self.sift_up(self.current_size)

  def sift_down(self, i):
    # if the current node has at least one child
    while (i * 2) <= self.current_size:
      # Get the index of the min child of the current node
      mc = self.min_child(i)
      # Swap the values of the current element is greater than its min child
      if self.heap_list[i] > self.heap_list[mc]:
          self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
      i = mc

  def min_child(self, i):
    # If the current node has only one child, return the index of the unique child
    if (i * 2)+1 > self.current_size:
      return i * 2
    else:
      # Herein the current node has two children
      # Return the index of the min child according to their values
      if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
          return i * 2
      else:
          return (i * 2) + 1

  def delete_min(self):
    # Equal to 1 since the heap list was initialized with a value
    if len(self.heap_list) == 1:
        return 'Empty heap'

    # Get root of the heap (The min value of the heap)
    root = self.heap_list[1]

    # Move the last value of the heap to the root
    self.heap_list[1] = self.heap_list[self.current_size]

    # Pop the last value since a copy was set on the root
    *self.heap_list, _ = self.heap_list

    # Decrease the size of the heap
    self.current_size -= 1

    # Move down the root (value at index 1) to keep the heap property
    self.sift_down(1)

    # Return the min value of the heap
    return root
"""
Driver program
"""
# Same tree as above example.
my_heap = MinHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)

print(my_heap.delete_min()) # removing min node i.e 5 

 
      