#!/bin/python3
# https://www.hackerrank.com/challenges/truck-tour/problem #

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(n, petrolpumps):
    # Write your code here
    start, passed, gas = 0, 0, 0
    while passed < n:
        station = petrolpumps.pop(0)
        gas += station[0]
        
        if gas >= station[1]:
            passed += 1
            gas -= station[1]
        else:
            start += passed + 1
            passed, gas = 0, 0
        petrolpumps.append(station)
    
    return start

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(n, petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()