# Given an array of integers, 
# find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. 
# The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

# array = [3, 4, -1, 1]
array = [1, 2, 0]

def findLowestPositiveInteger(array):
    num = 0
    array.sort()
    for i in range(array[0], len(array)):
        if i > 0 and i not in array:
            num = num + i
            return num
        elif i > 0 and i == array[-1]:
            num = i + 1
            return num

print(findLowestPositiveInteger(array))
    
