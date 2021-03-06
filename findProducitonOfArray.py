# Given an array of integers, 
# return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

import numpy as np
array = [1, 2, 3, 4, 5]
# array = [3, 2, 1]

def findProductionOfArray(array):
    resultArray = []
    
    for i in range(len(array)):
        tempArray=array.copy()
        tempArray.pop(i)
        resultArray.append(np.prod(tempArray))
    return resultArray

print(findProductionOfArray(array))