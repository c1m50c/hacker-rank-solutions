#!/bin/python3
# https://www.hackerrank.com/challenges/matrix-script/ #
# No `if` statements!

import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

result = ""
for x in zip(*matrix):
    result += "".join(x)
# Regular Expression is for finding AlphaNumeric Characters
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", result))