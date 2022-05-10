# Power digit sum
# Problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
# by Chinmoy Lenka of GeeksforGeeks

def calculate(n, power):
    return sum([int(i) for i in str(pow(n, power))])
     
# Driver Code
n = 2
power = 1000
print (calculate(n, power))