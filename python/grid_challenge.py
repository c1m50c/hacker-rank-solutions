#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/ #

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    a = [sorted(x) for x in grid]
    b = [list(x) for x in zip(*a)]
    c = [sorted(x) for x in b]
    if b == c:
        return "YES"
    return "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
