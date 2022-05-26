# [Trees]
# Binary Tree : each node can have up to 2 child nodes
# Binary Search Tree
# : each node is greater than every node in its left subtree
# : each node is less than every node in its right subtree
# BST Standard Operations
# insert, find, delete, get_size, traversals

# BST Insert
# - Start at root
# - Always insert as a leaf(very bottom node which doesn't have child node)
# BST Find
# - Start at root
# - Return the data if found, or False if not found
# BST Delete
# - 3 possibilities
# - which is leaf node : just delete the leaf node
# - which has 1 child node : promote the child to the target node's position
# - which has 2 child node : Find the next higher node, change delete target node and next higher node
# Get_size
# - returns number of nodes
# - works recursively
# - size = 1 + size(left subtree) + size (right subtree)
# [Traversal]
# Preorder Traversal
# : Visit root before visiting the root's subtrees
# Inorder Traversal
# : Visit root between visiting the root's subtrees. Gives values in sorted order.
# Advantages of Binary Search Tress?
# Because trees use recursion for most operations, they are fairly easy to implement.
# SPEED : Really fast locating data
# Insert, Delete, Find in O(h) = O(log n)
# In a balanced Binary Search Tree with 10,000,000 nodes would take 30 comparisons!

from doctest import TestResults


class Tree:
    # Constructor : sets three attributes - data, left subtree and right subtree.
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # Insert : inserts a new subtree into the proper location
    def insert(self, data):
        if self.data == data:
            return False # duplicate value
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True

    # Find : finds a value. If value not found, returns False
    def find(self,data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)
    
    # Get_size : returns the number of nodes in the tree(excluding None nodes).
    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1
        
    # Preorder : prints a preorder traversal of the tree.
    def preorder(self):
        if self is not None:
            print(self.data, end=' ')
            if self.left is not None:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    
    # Inorder : prints an inorder traversal of the tree.
    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.inorder()

# Test Code
# We create a new tree, insert one value, insert a whole list of values, find all values from 1 to 15
# (False for 0, 5, 8 shows that those values are not in the tree), print the size of the tree
# , print preorder and inorder traversals.

tree = Tree(7)
# print(tree.get_size())
# 1
tree.insert(9)
# print(tree.get_size())
# 2
for i in [15,10,2,12,3,1,13,6,11,4,14,9]:
    tree.insert(i)
# print(tree.get_size())
# 13
for i in range(16):
    print(tree.find(i), end=' ')
# print('\n', tree.get_size())
# False 1 2 3 4 False 6 7 False 9 10 11 12 13 14 15 
#  13
tree.preorder()
# 7 2 1 3 6 4 9 15 10 12 11 13 14
tree.inorder()
# 1 2 3 4 6 7 9 10 11 12 13 14 15

