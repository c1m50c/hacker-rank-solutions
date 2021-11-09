#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/ #

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes: list[int] = [0] * len(q)
    
    while sorted(q) != q:
        for i in range(0, len(q) - 1):
            j: int = len(q) - i - 1
            if q[j] < q[j - 1]:
                temp: int = q[j]
                q[j] = q[j - 1]
                q[j - 1] = temp
                bribes[q[j] - 1] += 1
    
    if max(bribes) >= 3: print("Too chaotic")
    else: print(sum(bribes))

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)