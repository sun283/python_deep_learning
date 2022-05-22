## Sequence Functions
# 1. Indexing starts with 0 for the first element
# String
x = 'frog'
# print out x of 3
# print(x[3])
#g

# list
x = ['pig', 'cow', 'horse']
# print(x[1])
# cow

# tuple
x = ('kevin', 'Niklas', 'Jenny', 'Craig')
# print(x[0])
# kevin

# 2. Slicing : slice out substrings, sublists, subtuples using indexes.
# [start : end +1 : step]
# start index item is inclusive, end index item in non inclusive
x = 'computer'
# omp
# print(x[1:4])
# opt
# print(x[1:6:2])
# puter
# print(x[3:])
# compu
# print(x[:5])
# r
# print(x[-1])
# ter
# print(x[-3:])
# comput
# print(x[:-2])

# 3. Adding / concatenating : combine 2 sequences of the same type by using +
# string
x = 'horse' + 'shoe'
# print(x)
# horseshoe

# list
y = ['pig', 'cow'] + ['horse']
# print(y)
# ['pig', 'cow', 'horse']

# tuple : the second tuple to be considered as tuple need to include a comma at the end
# if there is no comma at the end it is just a string in parentheses
z = ('Kevin', 'Niklas', 'Jenny') + ('Craig',)
# print(z)
# ('Kevin', 'Niklas', 'Jenny', 'Craig')

# 4. Multiplying : multiply a sequence using *
# string
x = 'bug' * 3
# print(x)
# bugbugbug

# list : multiplying the list by 3 times
y = [8,5] * 3
# print(y)
# [8,5,8,5,8,5]

# tuple
z = (2,4) * 3
# print(z)
# (2, 4, 2, 4, 2, 4)

# 5. Checking membership : test whether an item is or is not in the sequence.
# String
x = 'bug'
# print('u' in x)
# True

# list
y = ['pig', 'cow', 'horse']
# print('cow' not in y)
# False

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
# print('Niklas' in z)
# True

# 6. iterating : iterating through the items in a sequence.
# item
x = [7,8,3]
def printItem(x):
    for item in x:
        print(item)

# index & item using enumerate() function
# enumerate will return index and item together
y = [7,8,3]
def printItemAndIndex(y):
    for index, item in enumerate(y):
        print(index, item)
        
# 7. Number of items: count the number of items in a sequence
# Using len() function
# String
x = 'bug'
# print(len(x))
# 3

# list
y = ['pig', 'cow', 'horse']
# print(len(y))
# 3

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
# print(len(z))
# 4

# 8. Minimum : find the minimum item in a sequence lexicographically.
# Alpha or numeric types, but cannot mix types.
# find the smallest of the ASCII scale
# using the min() function on either alpha or numeric types
# you cannot mix alphabet and numeric into a same list or tuple
# String
x = 'bug'
# print(min(x))
# b

# list
y =  ['pig', 'cow', 'horse']
# print(min(y))
# cow

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
# print(min(z))
# Craig

# 9. Maximum : find the maximum item in a sequence lexicographically.
# Alpha and numeric types, but cannot mix types.
# String
# print(max(x))
# u

# list
# print(max(y))
# pig

# tuple
# print(max(z))
# Niklas

# 10. Sum : find the sum of items in a sequence. 
# Entire sequence must be numeric
# String -> error
x = [5, 7, 'bug']
# print(sum(x))

# list
y = [2,5,8,12]
# print(sum(y))
# 27
# print(sum(y[-2:]))
# 20

# tuple
z = (50,4,7,19)
# print(sum(z))
# 80


# 11. Sorting : returns a new list of items in sorted order.
# Does not change the original list.
# String
x = 'bug'
# print(sorted(x))
# ['b', 'g', 'u']

# list
y =  ['pig', 'cow', 'horse']
# print(sorted(y))
# ['cow', 'horse', 'pig']

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
# print(sorted(z))
# ['Craig', 'Jenny', 'Kevin', 'Niklas']

# 12. Sorting : sort by second letter
# using lambda function
# Add a key parameter and a lambda function to return the second character.
#(the word key here is a defined parameter name, k is an arbitrary variable name).
# print(sorted(z, key = lambda k : k[1]))
# ['Kevin', 'Jenny', 'Niklas', 'Craig']

# 13. Count(item) : returns count of an item
# String
x = 'hippo'
# print(x.count('p'))
# 2

# list
y =  ['pig', 'cow', 'horse', 'cow']
# print(y.count('cow'))
# 2

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
# print(z.count('Kevin'))
# 1

# 14. Index(item): returns the index of the first occurence of an item
# String
x = 'hippo'
# print(x.index('p'))
# 2

# list
y =  ['pig', 'cow', 'horse', 'cow']
# print(y.index('cow'))
# 1

# tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
# print(z.index('Jenny'))
# 2

# 15. Unpacking : unpack the n items of a sequence into n variables.
# number of variables exactly matches the length of that list or string
# String
x = 'pig'
a, b, c = x
# print(a, b, c)
# p i g

# list
y = ['pig', 'cow', 'horse']
a, b, c = y
# print(a, b, c)
# pig cow horse

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
a, b, c, d = z
# print(a, b, c, d)
# Kevin Niklas Jenny Craig

## Python Built-in Data Structures
# [Lists]
# - General purpose
# - Most widely used data structure
# - Grow and shrink size as needed
# - Sequence type
# - Sortable
# using square bracket

# 1. constructors : creating a new list
x = list()
# print(x)
# []

y = ['a', 25, 'dog', 8.43]
# print(y)
# ['a', 25, 'dog', 8.43]

tuple1 = (10, 20)
# print(tuple1)
# (10, 20)

z = list(tuple1)
# print(z)
# [10, 20]

# 2. list comprehension
a = [m for m in range(8)]
# print(a)
# [0, 1, 2, 3, 4, 5, 6, 7]

b = [i**2 for i in range(10) if i > 4]
# print(b)
# [25, 36, 49, 64, 81]

# 3. Delete : delete a list or an litem in a list
# using del()
x = [5,3,8,6]
del(x[1])
# print(x)
# [5, 8, 6]

del(x)
# print(x)
# list x no longer exists
# NameError: name 'x' is not defined

# 4. Append : append an item to a list
x = [5,3,8,6]
x.append(7)
# print(x)
# [5, 3, 8, 6, 7]

# 5. Extend : append a sequence to a list
# combining two seperate lists into one list
x = [5,3,8,6]
y = [12, 13]
# x.extend(y)
# print(x)
# [5, 3, 8, 6, 12, 13]

x = x + y
# print(x)
# [5, 3, 8, 6, 12, 13]

y.extend(x)
# print(y)
# [12, 13, 5, 3, 8, 6]

# 6. Insert : insert an item at a given index
x = [5,3,8,6]
x.insert(1, 7)
# print(x)
# [5, 7, 3, 8, 6]

x.insert(1,['a', 'm'])
# print(x)
# [5, ['a', 'm'], 7, 3, 8, 6]

# 7. Pop : pops last item off list and returns item
x = [5,3,8,6]
# pop off the 6
# return the result exclude popped item
x.pop()
# print(x)
# [5, 3, 8]

# return the popped item
# print(x.pop())
# 8

# 8. Remove : remove first instance of an item
x = [5,3,8,6,3]
x.remove(3)
# print(x)
# [5, 8, 6, 3]

# 9. Reverse : reverse the order of the list. 
# It is an in-place sort, meaning it changes the original list.
# it doesn't put in sorted order, simply reverse the list
x = [5,3,8,6]
x.reverse()
# print(x)
# [6, 8, 3, 5]

# 10. Sort : sort the list in place
# sorted(x) returns a new sorted list without changing the original list
# x.sort() puts the items of x in sorted order(sorts in place).
x = [5,3,8,6]
x.sort()
# print(x)
# [3, 5, 6, 8]

# 11. Reverse sort : sort items descending order.
# Use reverse=True parameter to the sort function
x = [5,3,8,6]
x.sort(reverse=True)
# print(x)
# [8, 6, 5, 3]

# [Tuples]
# Immutable(can't add/change)
# Useful for fixed data
# Faster than Lists
# Sequence type : all listed sequence functions above can be used.
# using parenthesis

# 1. constructors : creating new tuples.
x = ()
# print(x)
# ()

x = (1,2,3)
# print(x)
# (1, 2, 3)

x = 1,2,3
# print(x)
# (1, 2, 3)

x = 2,
# the comma tells Python htat it's tuple
# print(x, type(x))
# (2,) <class 'tuple'>

list1 = [2,4,6]
x = tuple(list1)
# print(x, type(x))
# (2, 4, 6) <class 'tuple'>

# 2. tuples are immutable, but member objects may be mutable.
x = (1,2,3)
# fails 'tuple' object doesn't support item deletion
# del(x[1])
# fails 'tuple' object does not support item assignment
# x[1] = 8

# a tuple where the first item is a list
y = ([1,2],3)
# delete the 2
# the list within the tuple is mutable
del(y[0][1])
# print(y)
# ([1], 3)

# 3. concatenating two tuples works
y += (4,)
# print(y)
# ([1], 3, 4)

# [Sets]
# - Store non-duplicate items(unique items are what sets are ideal for)
# - Very fast access vs lists
# to find an item in the list, need to compare list length times, 
# set hashes item, so it can find an item instantly using hash
# Great for checking membership
# - Math Set ops(union, intersect)
# - Sets are Unordered : you cannot sort

# 1. constructors: creating new sets
x = {3,5,3,5}
# print(x)
# {3, 5}

y = set()
# print(y)
# set()

list1 = [2,3,4]
z = set(list1)
# print(z)
# {2, 3, 4}
    
# 2. set operations
x = {3,5,8}
# print(x)
# {8, 3, 5}
x.add(7)
# print(x)
# {8, 3, 5, 7}

x.remove(3)
# print(x)
# {8, 5, 7}

# get length of set x
# print(len(x))
# 3

# check membership in x
# print(5 in x)
# True

# pop random item from set x
# print(x.pop(), x)
# 8 {5, 7}

# delete all items from set x
x.clear()
# print(x)
# set()

# 3. Mathematical set operations
s1 = {1,2,3}
s2 = {3,4,5}
# - intersection (AND) : set1 & set2
# print(s1 & s2)
# {3}

# - union(OR) : set1 | set2
# print(s1 | s2)
# {1, 2, 3, 4, 5} 

# - symmetric difference(XOR) : set1 ^ set2 difference 
# print(s1 ^ s2)
# {1, 2, 4, 5}

# (in set1 but not set2) : set1 - set2
# print(s1 - s2)
# {1, 2}

# - subset(set2 contains set1) : set1 <= set2
# print(s1 <= s2)
# False

# - superset(set1 contains set2) : set1 >= set2
# print(s1 > s2)
# False

# [Dictionaries(dict)]
# - Key/Value paris
# - Associative array, like JavaHashMap
# - Dicts are Unordered : you cannot sort
# they can be converted as list then sorted
# using curly braces

# 1. constructors : creating dictionaries
x = {'port': 25.3, 'beef': 33.8, 'chicken': 22.7}
# print(x)
# {'port': 25.3, 'beef': 33.8, 'chicken': 22.7}

x = dict([('port', 25.3), ('beef', 33.8), ('chicken', 22.7)])
# print(x)
# {'port': 25.3, 'beef': 33.8, 'chicken': 22.7}

x = dict(pork=25.3, beef=33.8, chicken=22.7)
# print(x)
# {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}

# 2. dict operations
# add or update item
x['shrimp'] = 38.2
# print(x)
# {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7, 'shrimp': 38.2}

x['shrimp'] = 38
# print(x)
# {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7, 'shrimp': 38}

# delete an item
del(x['shrimp'])
# print(x)
# {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}

# get length of dict x
# print(len(x))
# 3

# delete all items from dict x
x.clear()
# print(x)
# {}

# delete dict x
del(x)
# print(x)
# NameError: name 'x' is not defined

# 3. accessing keys and values in a dict
# Not compatible with Python2
y = {'port': 25.3, 'beef': 33.8, 'chicken': 22.7}

# print(y.keys())
# dict_keys(['port', 'beef', 'chicken'])

# print(y.values())
# dict_values([25.3, 33.8, 22.7])

# print(y.items())
# dict_items([('port', 25.3), ('beef', 33.8), ('chicken', 22.7)])

# check membership in y_keys(only looks in keys, not values)
# print('beef' in y)
# True

# check membership in y_values
# print('clams' in y.values())
# False

# iterating a dict : note, items are in random order.
def printKeyValue():
    for key in y:
        print(key, y[key])
# port 25.3
# beef 33.8
# chicken 22.7

# item will return a tuple which has a key and a value pair
def printKeyValue2():
    for k, v in y.items():
        print(k, v)
# port 25.3
# beef 33.8
# chicken 22.7

