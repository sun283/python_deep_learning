# Given a list of numbers and a number k, 
# return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

array = [10, 15, 3, 7]
sum = 17

def findPairForSum(array, sum):
    global num1, num2
    i = 0
    j = len(array)-1
    array.sort()

    while i < j:
        if array[i] + array[j] == sum:
            num1 = array[i]
            num2 = array[j]
            return True
        elif array[i] + array[j] < sum:
            i = i +1
        else:
            j = j -1
    return False

print(findPairForSum(array, sum))
print(num1, num2)
