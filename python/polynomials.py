# https://www.hackerrank.com/challenges/np-polynomials/problem #

import numpy

arr = list(map(float,input().split()))
x = float(input())

print(numpy.polyval(arr, x))