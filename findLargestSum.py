# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
# Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

import sys
 
# Function to calculate the maximum sum in a given list
# with no adjacent elements considered
# `i` ——> index of the current element
# `prev` ——> index of the previous element included in the sum
def findMaxSumSubsequence(nums, i, n, prev=-sys.maxsize):
    print('i=',i)
    # base case: all elements are processed
    if i == n:
        print('if i=',i)
        return 0
 
    # recur by excluding the current element
    excl = findMaxSumSubsequence(nums, i + 1, n, prev)
    # print('excl=',excl)
    print('excl i=',i)
    # print('n=',n)
    # print('prev', prev)
    incl = 0
 
    # include current element only if it's not adjacent to
    # the previous element
    if prev + 1 != i:
        print('incl i=',i)
        incl = findMaxSumSubsequence(nums, i + 1, n, i) + nums[i]
 
    # return maximum sum we get by including or excluding current item
    return max(incl, excl)
 
if __name__ == '__main__':
    nums = [1, 2, 9, 4, 5, 0, 4, 11, 6]
    print('The maximum sum is', findMaxSumSubsequence(nums, 0, len(nums)))
