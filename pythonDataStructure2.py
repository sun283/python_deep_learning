# import randam

# Python List Comprehension
# basin format: new_list = [transform sequence[filter]]

# get values within a range
under_10 = [x for x in range(10)]
# print('under_10: '+str(under_10))
# under_10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# get squared values
squares = [x**2 for x in under_10]
# print('squares: '+ str(squares))
# squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# get odd numbers using mod
odds = [x for x in range(10) if x % 2 == 1]
# print('odd: '+str(odds))
# odd: [1, 3, 5, 7, 9]

# get multiples of 10
ten_x = [x * 10 for x in range(10)]
# print('ten_x: '+str(ten_x))
# ten_x: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# get all numbers from a string
s = 'I love 2 go t0 the store 7 times a w3ek.'
nums = [x for x in s if x.isnumeric()]
# print('nums: '+ str(nums))
# nums: ['2', '0', '7', '3']

# print('nums: '+''.join(nums))
# nums: 2073

# get index of a list item
names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
idx = [k for k, v in enumerate(names) if v == 'Anu']
# print(idx)
# [2]

# print('index: '+ str(idx[0]))
# index: 2

# delete an item from a list
from os import popen
import random
from re import M
from turtle import position
letters = [x for x in 'ABCDEF']
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
# print(letters, letrs)
# ['D', 'C', 'F', 'A', 'B', 'E'] ['D', 'F', 'A', 'B', 'E']

# nested loop iteration for 2D list
# b is the subsets, x is the values
a = [[1,2], [3,4]]
new_list = [b for b in a]
# print(new_list)
# [[1, 2], [3, 4]]

new_list = [x for b in a for x in b]
# print(new_list)
# [1, 2, 3, 4]

# Stacks, Queues, Heaps
# [Stacks]
# LIFO : last in, first out data structure
# Push : push an item onto the stack
# Pop : pop an item off of the stack
# All push and pop operations are to/from the top of the stack.
# Peek : get item on top of stack, without removing it.
# Clear all items from stack
# Use append() to push an item onto the stack
# Use pop() to remove an item

# Stack use case
# undo : track which commands have been executed.
# pop last command off command stack to undo it.

my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
# print(my_stack)
# [4, 7, 12, 19]
# print(my_stack.pop())
# 19
# print(my_stack.pop())
# 12
# print(my_stack)
# [4, 7]

# Stack using List with a Wrapper Class
# 자료형(primitive data types)에 대한 클래스 표현을 래퍼 클래스(wrapper classes)라고 합니다.
# 기본 자료형에 대해서 객체로서 인식되도록 '포장'을 했다는 뜻입니다. 
# 객체라는 상자에 기본 자료형을 넣은 상태로 생각하면 됩니다. 
# 필요시 컴파일러가 자동으로 수행하기 때문에 이를 오토박싱(autoboxing)이라고 합니다.
# 메소드의 인수로 객체 타입만이 요구되면, 기본 타입의 데이터를 그대로 사용할 수는 없습니다.
# 이때에는 기본 타입의 데이터를 먼저 객체로 변환한 후 작업을 수행해야 합니다.
# 기본 타입에 해당하는 데이터를 객체로 포장해 주는 클래스를 래퍼 클래스(Wrapper class)라고 합니다.
# 래퍼 클래스는 각각의 타입에 해당하는 데이터를 인수로 전달받아, 해당 값을 가지는 객체로 만들어 줍니다.
# 기본 타입의 데이터를 래퍼 클래스의 인스턴스로 변환하는 과정을 박싱(Boxing)이라고 합니다.
# 반면 래퍼 클래스의 인스턴스에 저장된 값을 다시 기본 타입의 데이터로 꺼내는 과정을 언박싱(UnBoxing)이라고 합니다.
# We create a Stack and a full set of Stack methods.
# But the underlying data structure is really a Python List
# For pop and peek methods we first check whether the stack is empty, to avoid exceptions.
class Stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)
    
# Test code for Stack Wrapper Class
my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
# print(my_stack)
# [1, 3]

# print(my_stack.pop())
# 3
# print(my_stack)
# [1]

# print(my_stack.peek())
# 3
# print(my_stack)
# [1, 3]

# print(my_stack.pop())
# print(my_stack.pop())
# print(my_stack.pop())
# 3
# 1
# None

# [Queues]
# Enqueue : add an item to the end of the line
# Dequeue : remove an item from the front of the line.
# FIFO : First-in First-out
# Enqueue on one end, Dequeue from the other end.

# Queues Use Cases
# Queues are good for modeling anything you wait in line for
# Bank tellers. Placing an order at McDonals.
# DMV customer service. Supermarket checkout.
# Dequeue is a double-ended queue, but we can use it for our queue.
# We use append() to enqueue an item, and popleft() to dequeue an item.

# 이 모듈은 파이썬의 범용 내장 컨테이너 dict, list, set 및 tuple에 대한 대안을 제공하는 특수 컨테이너 데이터형을 구현합니다.
from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
# print(my_queue)
# deque([5, 10])
# print(my_queue.popleft())
# 5

# [Heaps]
# What is a MaxHeap?
# Complete Binary Tree
# Every node <= its parent
# Remove Max in O(log n)
# Insert in O(log n)
# Get Max in O(1)

# Every node of tree has to be less than its parent
# If we pop the last number of the heap, we know that its the highest number in that heap
# the highest number always rises to the top of the heap
# Max Heap is easy to implement using a List

# i = 4
# parent(i) = i/2 = 2
# left(i) = i*2 = 8
# right(i) = i * 2 + 1 = 9

# MaxHeap operations
# push(insert)
# - add value to end of array
# - Float it up to its proper position(compare with parent node)
# peek(get max)
# - return the value at heap[1]
# pop(remove max)
# - Move Max to end of array
# - Delete it
# - Bubble Down the item at index 1 to its proper position(Compare with child node)
# - Return max

# Python MaxHeap
# A MaxHeap always bubbles the highest value to the top, 
# so it can be removed instantly
# Public functions: push, peek, pop
# Private functions: swap, __floatUp, __bubbleDown, __str.
class MaxHeap:
    def __init__(self, items=[]):
        super().__init__
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def __floatUp(self, index):
        parent = index 
        # 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest - right        
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)
    def __str__(self):
        return str(self.heap)

# MaxHeap test code
m = MaxHeap([95,3,21])
m.push(10)
# print(m)
# [0, 95, 3, 21, 10]

print(m.pop())
# 95

print(m.peek())
# 10?
