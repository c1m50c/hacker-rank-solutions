# https://www.hackerrank.com/challenges/np-linear-algebra/problem #

import numpy

n = int(input())
arrays: list[list[float]] = [  ]
for _ in range(0, n):
    arrays.append(list(map(float, input().split())))

print(round(numpy.linalg.det(arrays), 2))