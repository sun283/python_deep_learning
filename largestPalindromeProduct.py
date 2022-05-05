# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# A palindromic number or numeral palindrome is a number that remains the same when its digits are reversed. 
# Like 16461, for example, it is "symmetrical". 
# The term palindromic is derived from palindrome, which refers to a word (such as rotor or racecar) whose spelling is unchanged when its letters are reversed. 
# The first 30 palindromic numbers (in decimal) are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, …
# The largest palindrome made from the product of two 3-digit numbers is 913 * 993 = 906609.
# Note: 9999 * 9901 = 906609

n = 0
for a in range(1,1000):
    for b in range(a, 1000):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
print(n)
