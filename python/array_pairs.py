#!/bin/python3
# https://www.hackerrank.com/challenges/array-pairs/ #
# This solution should work, but will run into timeouts sadly #

import os

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solve(arr):
    result: int = 0
    n: int = len(arr)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[i] * arr[j] <= max(arr[i : j + 1]):
                result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
