# There are a collection of numbers. 
# I need you to take this collection of numbers
# and find a matching pair that is equal to a sum that I give you as well
# The numbers are in memory and you can go with an array
# You can also assume that they're ordered
# You can't repeat the same element at the same index twice
# THe same number may appear twice
# You can assume that they'll always be integers
# Negatives could happen
# The range number in the same array : first number is the smallest and last number is the biggest

# Test
sum = 8
arr = [1,2,3,9]
arr2 = [1,2,4,4]

# Solution 1. 2 for loops (Quadratic)
# I don't repeat the smae value
# Just testing all of them if the sum is equal to the target sum
# It's time-consuming
def solutionOne(array, sum):
    for i in range(len(array) - 1):
        # start from the i'th element until the last element
        for j in range(i + 1, len(array)):
            # if the desired sum is found, print it
            if array[i] + array[j] == array:
                print('Pair found', (array[i],",", array[j]))
                return True
            else:
                return False

# Solution 2. Binary Search(Unidirectional)
# Still slow
def solutionTwo(array, sum):
    i = 0
    size = len(array)
    while i < size:
        if i + array[i:size] == sum:
            print('Pair found', (array[i],",", sum - array[i]))
            return True
        else:
            i += 1
    return False

# Solution 3,4 would be preferred
# Solution 3. Linear search
def solutionThree(array, sum):
    size = len(array)
    i,j = 0, size-1
    while 1 < size and j < size and i < j:
        if i != j and array[i] + array[j] == sum:
            print('Pair found', (array[i],",", array[j]))
            return True
        elif array[i] + array[j] > sum:
            j -= 1
        else :
            i += 1
    print("No pair found")
    return False

# Additional
# Can not guarentee that the numbers are sorted
# Solution 4. 
def solutionFour(array, sum):
    compliment = []
    for i in array:
        if(compliment.index(sum - i) != len(compliment)):
            return True
        compliment.append(sum - i)
    return False