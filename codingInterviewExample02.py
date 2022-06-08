from operator import truediv

array = [1,2,4,4]
# array = [1,2,3,9]
sum = 8
i = 0
j = 1

def solution1(array, sum):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            print(array[i], "+", array[j], "=", array[i]+array[j])
            if array[i] + array[j] == sum:
                return (True, array[i], ",", array[j])
    return False

# print(solution1(array, sum))

def solution2(array, sum):
    for i in range(len(array)):
        s = sum - array[i]
        # print(s)
        if s in array[i+1 : len(array)]:
            return (True, array[i], s)
    return False
# print(solution2(array, sum))

def solution3(array, sum):
    i = 0
    j = len(array)-1
    for i in range(len(array)):
        if array[i] + array[j] > sum:
            j = j - 1
        elif array[i] + array[j] < sum:
            i = i + 1
        elif array[i] + array[j] == sum:
            return (array[i] , " + ", array[j], "=", array[i] + array[j])
    return False
# print(solution3(array, sum))

def solution4(array, sum):
    i = 0
    j = len(array)-1
    while i < j:
        if array[i] + array[j] > sum:
            j = j - 1
        elif array[i] + array[j] < sum:
            i = i + 1
        elif array[i] + array[j] == sum:
            return (array[i] , " + ", array[j], "=", array[i] + array[j])
    return False
# print(solution4(array, sum))


arry = [3,9,1,2]
# arry = [4,1,2,4]
def solution5(arry, sum):
    arry.sort()
    
    i = 0
    j = len(arry)-1
    while i < j:
        if arry[i] + arry[j] > sum:
            j = j - 1
        elif arry[i] + arry[j] < sum:
            i = i + 1
        elif arry[i] + arry[j] == sum:
            return (arry[i] , " + ", arry[j], "=", arry[i] + arry[j])
    return False
# print(solution5(arry, sum))

def solution6(arry, sum):
    complement = []
    for i in range(len(arry)):
        s = sum - arry[i]
        if s in complement:
            return True
        else:
            complement.append(arry[i])
    return False        
# print(solution6(arry, sum))

