#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-tower-breakers-1/ #

"""
    https://www.hackerrank.com/challenges/one-week-preparation-kit-tower-breakers-1/forum/comments/1038689
    🔼 The comment above helps explain the solution very well, as the provided base explanation is difficult to grasp at first.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    if m == 1: # Player 2 wins
        return 2

    wins: list[int] = [ 0, 0 ] # 0: Player1, 1: Player2
    for tower in range(1, n + 1):
        if tower % 2 == 0: # Player 1 Goes first, Player 2 Wins
            wins[1] += 1
        else: # Player 2 Goes first, Player 1 Wins
            wins[0] += 1
    
    if wins[0] > wins[1]:
        return 1
    return 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()