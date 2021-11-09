#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/ #

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    if k == 0: return s
    result: str = ""

    for i in range(0, len(s)):
        character = s[i]
        if character.isalpha():
            if character.islower():
                character = (ord(character) + k - 97) % 26 + 97
            else:
                character = (ord(character) + k - 65) % 26 + 65
            character = chr(character)
        result += character
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()